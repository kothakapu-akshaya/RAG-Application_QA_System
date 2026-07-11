import { useState } from "react";
import { queryDocument } from "../services/query";

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

  const handleSend = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

    // Display user's question
    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");

    try {
      const response = await queryDocument(userQuestion);

      // Display bot's answer
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Something went wrong while getting the answer.",
        },
      ]);
    }
  };

  return (
    <section>
      <h2>Chat</h2>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask something about your uploaded document..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={handleSend}>Send</button>
      </div>

      <div className="chat-box">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            <strong>
              {message.sender === "user" ? "You" : "Document Assistant"}:
            </strong>
            <br />
            {message.text}
          </div>
        ))}
      </div>
    </section>
  );
}

export default ChatWindow;