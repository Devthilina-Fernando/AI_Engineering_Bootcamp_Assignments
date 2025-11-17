import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'VitalVibe - Your Daily Health Companion',
  description: 'Get personalized health tips based on your daily routine',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}

