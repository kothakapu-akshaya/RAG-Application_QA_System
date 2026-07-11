import { useState } from "react";

type Message = {
  sender: "user" | "Raccon";
  text: string;
};

function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "Raccon",
      text: "Hey 👋! Upload a PDF document and ask me a question to get clarity.",
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

  <div className="chat-input">
    <input
      type="text"
      placeholder="Ask a question..."
      value={question}
      onChange={(e) => setQuestion(e.target.value)}
    />

    <button onClick={handleSend}>Send</button>
  </div>

  <div className="chat-box">
    {messages.map((message, index) => (
      <div key={index} className={`message ${message.sender}`}>
        <strong>{message.sender === "user" ? "You" : "Racoon"}:</strong>
        <br />
        {message.text}
      </div>
    ))}
  </div>
</section>
  );
}

export default ChatWindow;
