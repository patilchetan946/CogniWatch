# CogniWatch - Final Year Project

## 📌 Overview
CogniWatch is an advanced scene analysis and public safety system that uses **Convolutional Neural Networks (CNN)** to detect anomalies in real-time. It provides automated alerts via **Email API and Twilio API**, ensuring timely notifications for potential security threats.

## 🚀 Features
- 🎥 **Real-time anomaly detection** using CNN
- 📩 **Automated email alerts** for detected anomalies
- 📞 **Twilio API integration** for SMS/Call notifications
- 🖥️ **Tkinter-based GUI** for easy interaction
- 🛡️ **Enhances public safety** with quick response alerts
- 📊 **Data logging and analytics** for performance tracking
- 🖼️ **Customizable detection settings** based on sensitivity levels
- 🔧 **Easy integration** with external security systems

## 🛠️ Technologies Used
- **Python** (Core development)
- **Keras & TensorFlow** (CNN model)
- **OpenCV** (Image processing)
- **Email API** (Alert notifications)
- **Twilio API** (SMS/Call notifications)
- **Tkinter** (User Interface)
- **Matplotlib & Seaborn** (Data visualization)
- **SQLite/PostgreSQL** (Database for logs and records)

## 📂 Project Structure
```bash
CogniWatch-FinalYearProject/
│-- dataset/                  # Training data
│-- models/                   # Saved CNN models
│-- gui/                      # Tkinter-based UI components
│-- scripts/                  # Utility scripts
│-- logs/                     # Stored logs and reports
│-- main.py                   # Main application script
│-- requirements.txt          # Dependencies
│-- config.json               # Configuration settings
│-- README.md                 # Project documentation
│-- Background/
│-- Suspicious/
│-- .gitignore
│-- CNNModel.py
│-- Font.py
│-- Forget_password.py
│-- GUI_Main.py
│-- GUI_Master.py
│-- Train_FDD_cnn.py
│-- abnormalevent.h5
│-- call.py
│-- detection.py
│-- evaluation.db
│-- face.db
│-- login.py
│-- mail.py
│-- mail2.py
│-- registration.py
```

## 📦 Libraries Used
- **numpy** - Numerical computing
- **os** - Operating system interactions
- **gc** - Garbage collection
- **PIL (Pillow)** - Image processing
- **tqdm** - Progress bar for loops
- **tkinter** - GUI development
- **csv** - Handling CSV files
- **datetime** - Date and time utilities
- **time** - Time-related functions
- **cv2 (OpenCV)** - Computer vision tasks
- **shutil** - File operations
- **skimage.measure** - Image measurement utilities
- **sqlite3** - Database management
- **tkvideo** - Video handling in Tkinter

## 🔧 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Saurbhmoynak/CogniWatch-FinalYearProject.git
   OR
   git clone https://github.com/patilchetan946/CogniWatch.git
   cd CogniWatch-FinalYearProject
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## 📊 Data Logging & Monitoring
- All detected anomalies are logged in a database.
- Visualize trends using `logs_analysis.py`.
- Export logs in CSV format for external analysis.

## 🛠️ Configuration
- Modify `config.json` to customize thresholds and alert settings.
- Adjust model sensitivity for better detection accuracy.

## 📧 Contact
For queries or contributions, reach out at: **saurbhmoynak012@gmail.com**,**patilchetan946@gamil.com**

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
