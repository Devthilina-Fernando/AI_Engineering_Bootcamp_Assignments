'use client'

import { useState } from 'react'
import axios from 'axios'
import styles from './page.module.css'

interface HealthTipsResponse {
  tips: string
  user_input: string
}

export default function Home() {
  const [description, setDescription] = useState('')
  const [tips, setTips] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!description.trim()) {
      setError('Please describe your day')
      return
    }

    setLoading(true)
    setError(null)
    setTips(null)

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
      const response = await axios.post<HealthTipsResponse>(
        `${apiUrl}/api/health-tips`,
        { description: description.trim() }
      )
      
      setTips(response.data.tips)
      setDescription('')
    } catch (err: any) {
      setError(
        err.response?.data?.detail || 
        'Failed to get health tips. Please try again.'
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.header}>
          <h1 className={styles.title}>
            <span className={styles.titleIcon}>✨</span>
            VitalVibe
          </h1>
          <p className={styles.subtitle}>
            Your Daily Health Companion
          </p>
          <p className={styles.description}>
            Tell us about your day and get personalized health tips tailored just for you
          </p>
        </div>

        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.inputGroup}>
            <textarea
              className={styles.textarea}
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="e.g., busy meetings today, skipped breakfast, feeling tired..."
              rows={4}
              disabled={loading}
            />
          </div>

          <button
            type="submit"
            className={styles.submitButton}
            disabled={loading || !description.trim()}
          >
            {loading ? (
              <>
                <span className={styles.spinner}></span>
                Getting your tips...
              </>
            ) : (
              <>
                <span>💡</span>
                Get Health Tips
              </>
            )}
          </button>
        </form>

        {error && (
          <div className={styles.error}>
            <span>⚠️</span>
            {error}
          </div>
        )}

        {tips && (
          <div className={styles.tipsContainer}>
            <div className={styles.tipsHeader}>
              <h2>Your Personalized Health Tips</h2>
              <button
                className={styles.closeButton}
                onClick={() => setTips(null)}
                aria-label="Close tips"
              >
                ×
              </button>
            </div>
            <div className={styles.tipsContent}>
              {tips.split('\n').map((tip, index) => (
                tip.trim() && (
                  <div key={index} className={styles.tip}>
                    <span className={styles.tipIcon}>💚</span>
                    <p>{tip.trim()}</p>
                  </div>
                )
              ))}
            </div>
          </div>
        )}

        <div className={styles.footer}>
          <p>Powered by AI • Made with ❤️ for your wellness</p>
        </div>
      </div>
    </main>
  )
}

