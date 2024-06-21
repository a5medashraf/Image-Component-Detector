import streamlit as st
from PIL import Image
from ultralytics import YOLO



# Yolo Model and the model results
model = YOLO('yolov5su.pt')

def analyze_image(image):
    results = model(image)
    detectedClasses = results[0].boxes.cls.cpu().numpy()
    detectedComponents = [results[0].names[oneClass] for oneClass in detectedClasses ]
    return detectedComponents




# Stramlit Interface
st.title("Image Component Detector")    
st.write("Upload an image and click 'Analyze Image' to detect components in the image.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button("Analyze Image"):
        st.write("Analyzing the image...")
        components = analyze_image(image)
        st.write("Detected components:", components)
