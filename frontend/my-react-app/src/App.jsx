import { useState } from 'react'
import babyLogo from '/baby.svg'
import cribLogo from '/crib.svg'
import listenLogo from '/listen.svg'
import logoLogo from '/logo.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <img src={logoLogo} className="logo" alt="brand logo" />
      </div>
      <div className="icon-container">
        <div className="icon-item">
          <a href="https://react.dev" target="_blank">
            <img src={listenLogo} className="logo" alt="listen logo" />
          </a>
          <p>tear analysis</p>
        </div>
        <div className="icon-item">
          <a href="https://6xk88r85-8501.use.devtunnels.ms/" target="_blank">
            <img src={babyLogo} className="logo" alt="baby logo" />
          </a>
          <p>baby monitor</p>
        </div>
        <div className="icon-item">
          <a href="https://react.dev" target="_blank">
            <img src={cribLogo} className="logo" alt="crib logo" />
          </a>
          <p>crib safety</p>
        </div>
      </div>
      <h1>Smarter Monitoring for Safer Sleep.</h1>
      <h2>AI-powered metrics that listen to, learn from, and protect your child</h2>
      <p>
        Because your child deserves a restful night, and so do you.
      </p>
    </>
  )
}

export default App
