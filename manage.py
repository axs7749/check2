<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Assistant Reply</title>
</head>
<body>
    <h1>Assistant Reply</h1>
    <div id="assistant-reply"></div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Use the messages array from your Python code and pass the last message into the JavaScript context
            const replyFromAssistant = "messages"; // Replace with `messages[-1].content[0].text.value` from your Python code block.
            // Set the assistant reply in the div with the ID 'assistant-reply'
            document.getElementById('assistant-reply').innerText = replyFromAssistant;
        });
    </script>
</body>
</html>