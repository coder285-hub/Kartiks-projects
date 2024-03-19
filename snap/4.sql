SELECT users.username
FROM users u
JOIN (
    SELECT to_user_id, COUNT(*) AS message_count
    FROM messages
    GROUP BY to_user_id
) AS message_counts ON users.id = message_counts.to_user_id
ORDER BY message_counts.message_count DESC, u.username ASC
LIMIT 1;
