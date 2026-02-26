<h1 align="center">🖐️ Virtual Writer using Hand Gesture Recognition</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Currently%20Developing-brightgreen" alt="Status Badge"/>
</p>

<hr>

<h2>🚀 Overview</h2>

<p>
Virtual Writer is a real-time hand gesture–based drawing application built using 
<strong>OpenCV</strong> and <strong>MediaPipe</strong>.
</p>

<p>It allows users to:</p>

<ul>
  <li>✋ Raise <strong>1 finger</strong> → Activate <strong>Pen Mode</strong></li>
  <li>✌️ Raise <strong>2 fingers</strong> → Activate <strong>Eraser Mode</strong></li>
  <li>Use index fingertip as a virtual pen</li>
  <li>Draw in the air on a digital canvas</li>
</ul>

<p>
This project uses computer vision and hand landmark detection to create a touchless writing experience using just a webcam.
</p>

<hr>

<h2>🧠 How It Works</h2>

<ol>
  <li>Webcam captures live video feed.</li>
  <li>MediaPipe detects 21 hand landmarks.</li>
  <li>Finger positions are analyzed to determine gesture.</li>
  <li>Based on gesture:
    <ul>
      <li>Drawing mode is activated</li>
      <li>Erasing mode is activated</li>
    </ul>
  </li>
  <li>Drawing is rendered on a virtual canvas overlay.</li>
</ol>

<hr>

<h2>🛠️ Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
  <li>NumPy</li>
</ul>

<hr>

<h2>📂 Project Structure (Planned)</h2>

<pre>
virtual_writer/
│
├── main.py
├── hand_tracking.py
├── utils.py
├── README.md
</pre>

<hr>

<h2>🔥 Features (Planned & In Progress)</h2>

<ul>
  <li>✅ Real-time hand detection</li>
  <li>⬜ Finger counting logic</li>
  <li>⬜ Pen mode (1 finger)</li>
  <li>⬜ Eraser mode (2 fingers)</li>
  <li>⬜ Smooth drawing</li>
  <li>⬜ Color selection</li>
  <li>⬜ Save canvas as image</li>
  <li>⬜ UI overlay improvements</li>
</ul>

<hr>

<h2>🎯 Goal</h2>

<p>
To build a fully interactive air-writing system that feels natural, smooth, and responsive — without any physical touch.
</p>

<hr>

<h2>📌 Current Status</h2>

<p>
<span style="color:green; font-weight:bold;">🟢 Currently Developing</span>
</p>

<p>
Core hand tracking is implemented. Gesture recognition and drawing functionality are under development.
</p>

<hr>

<h2>💡 Future Enhancements</h2>

<ul>
  <li>AI-based handwriting recognition</li>
  <li>Gesture-based tool switching</li>
  <li>Web-based version</li>
  <li>Performance optimization</li>
  <li>Multi-hand support</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>
This project is open-source and available under the MIT License.
</p>