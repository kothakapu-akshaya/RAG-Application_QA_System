import { useState } from "react";

type Message = {
  sender: "user" | "bot";
  text: string;
};

function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "bot",
      text: "Hello! Upload a document and ask me a question.",
    },
  ]);

  const [question, setQuestion] = useState("");

  const handleSend = () => {
    if (!question.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: question,
      },
    ]);

    setQuestion("");
  };

  return (
    <section>
      <h2>Chat</h2>

      <div className="chat-box">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            <strong>{message.sender === "user" ? "You" : "Bot"}:</strong>{" "}
            {message.text}
          </div>
        ))}
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={handleSend}>Send</button>
      </div>
    </section>
  );
}

export default ChatWindow;
