# SIHH Project - Streamlit Deployment Guide

## Quick Start

### Local Development
1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Deploy to Streamlit Cloud

1. **Push to GitHub:**
   - Create a new repository on GitHub
   - Push your code:
     ```bash
     git init
     git add .
     git commit -m "Initial commit: SIHH Streamlit app"
     git branch -M main
     git remote add origin https://github.com/yourusername/sihh-project.git
     git push -u origin main
     ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy!"

3. **Alternative Deployment Options:**
   - **Heroku:** Use the provided `Procfile`
   - **Railway:** Direct GitHub integration
   - **Render:** Simple web service deployment

### Environment Variables
For production deployment, set these environment variables:
- `STREAMLIT_SERVER_PORT`: Server port (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)

### Features Included
- 🏠 **Home Page:** Project overview and interactive demo
- 📊 **Dashboard:** Metrics and data visualization
- 📈 **Analytics:** Field distribution and success rates
- ⚙️ **Settings:** Application configuration

### Project Structure
```
SIHH/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/           # Streamlit configuration
│   └── config.toml
├── src/                  # React source (if needed)
├── package.json          # Node.js dependencies (React)
└── README.md            # Project documentation
```

### Customization
- Modify `app.py` to add your specific SIHH project features
- Update the theme colors in `.streamlit/config.toml`
- Add your own data sources and ML models
- Customize the UI components and layouts

### Support
For deployment issues or questions, refer to:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Cloud](https://streamlit.io/cloud)