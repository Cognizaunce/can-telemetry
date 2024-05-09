from logger import Logger


class SQLiteLogger(Logger):
    """Concrete implementation of Logger for SQLite logging."""

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def log_message(self, message):
        # Implementation specific to SQLite logging
        pass

    def sqlite_read_via(
            self,
            n: int,
            white_list_ids: list = None,
            black_list_ids: list = None,
            is_error_frame: bool = None,
    ) -> list[can.Message]:
        """General purpose CAN message query function from SQLite database.

        Args:
            n: Number of messages to fetch.
            white_list_ids: List of arbitration IDs to include.
            black_list_ids: List of arbitration IDs to exclude.
            is_error_frame: If messages should be filtered by error state.

        Returns:
            list: List of can.Message objects from SQLite cursor fetchall query.

        Notes:
            Database fields:
                timestamp       =   ts
                arbitration_id  =   arbitration_id
                is_extended_id  =   extended
                is_remote_frame =   remote
                is_error_frame  =   error
                dlc             =   dlc
                data            =   data
        """
        # Construct the query.
        query = (
            "SELECT ts, arbitration_id, extended, remote, error, dlc, data "
            "FROM messages"
        )
        conditions = []
        parameters = []

        # Setup database connector and cursor.
        connector = sqlite3.connect(self.sqlite_log_file_path)
        cursor = connector.cursor()

        # Filter by white list and black list of arbitration IDs.
        if white_list_ids:
            placeholders = ",".join("?" for _ in white_list_ids)
            conditions.append(f"arbitration_id IN ({placeholders})")
            parameters.extend(white_list_ids)
        if black_list_ids:
            placeholders = ",".join("?" for _ in black_list_ids)
            conditions.append(f"arbitration_id NOT IN ({placeholders})")
            parameters.extend(black_list_ids)

        # Filter by is_error_frame if specified.
        if is_error_frame is not None:
            conditions.append("is_error_frame = ?")
            parameters.append(is_error_frame)

        # Append conditions to query if any.
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Append ordering and limit.
        query += " ORDER BY ts DESC LIMIT ?"
        parameters.append(n)

        # Execute the query.
        cursor.execute(query, parameters)
        rows = cursor.fetchall()

        # Close cursor and connector.
        cursor.close()
        connector.close()

        # Convert rows to can.Message objects.
        messages = []
        for row in rows:
            message = can.Message(
                timestamp=row[0],
                arbitration_id=row[1],
                is_extended_id=row[2],
                is_remote_frame=row[3],
                is_error_frame=row[4],
                dlc=row[5],
                data=row[6],
            )
            # Augment the message object with attribute.
            messages.append(message)

        return messages