'use client'

import { useState, useRef, useEffect } from 'react'
import axios from 'axios'
import styles from './page.module.css'

interface Message {
  role: 'user' | 'assistant'
  content: string
  imageUrl?: string
  location?: string
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: "Hello! I'm your weather assistant. Ask me about the weather in any location! 🌤️",
    },
  ])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage: Message = {
      role: 'user',
      content: input,
    }

    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const conversationHistory = messages.map((msg) => ({
        role: msg.role,
        content: msg.content,
      }))

      const response = await axios.post('http://localhost:8000/api/chat', {
        message: input,
        conversation_history: conversationHistory,
      })

      const assistantMessage: Message = {
        role: 'assistant',
        content: response.data.response,
        imageUrl: response.data.image_url,
        location: response.data.location,
      }

      setMessages((prev) => [...prev, assistantMessage])
    } catch (error: any) {
      console.error('Error:', error)
      const errorMessage: Message = {
        role: 'assistant',
        content: `Sorry, I encountered an error: ${error.response?.data?.detail || error.message}. Please try again.`,
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.header}>
          <h1 className={styles.title}>🌤️ Weather Chatbot</h1>
          <p className={styles.subtitle}>Ask me anything about the weather!</p>
        </div>

        <div className={styles.chatContainer}>
          <div className={styles.messages}>
            {messages.map((message, index) => (
              <div
                key={index}
                className={`${styles.message} ${
                  message.role === 'user' ? styles.userMessage : styles.assistantMessage
                }`}
              >
                <div className={styles.messageContent}>
                  {message.location && message.role === 'assistant' && (
                    <div className={styles.locationBadge}>
                      📍 {message.location}
                    </div>
                  )}
                  <p>{message.content}</p>
                  {message.imageUrl && (
                    <div className={styles.imageContainer}>
                      <img
                        src={message.imageUrl}
                        alt="Weather visualization"
                        className={styles.weatherImage}
                      />
                    </div>
                  )}
                </div>
              </div>
            ))}
            {isLoading && (
              <div className={`${styles.message} ${styles.assistantMessage}`}>
                <div className={styles.messageContent}>
                  <div className={styles.loading}>
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <form onSubmit={handleSubmit} className={styles.inputForm}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about the weather..."
              className={styles.input}
              disabled={isLoading}
            />
            <button
              type="submit"
              className={styles.sendButton}
              disabled={isLoading || !input.trim()}
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
            </button>
          </form>
        </div>
      </div>
    </main>
  )
}

