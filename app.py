import streamlit as st
from PIL import Image , ImageEnhance
from PIL.ImageFilter import *

#Page settings
st.set_page_config(page_title="Image Editor App")
st.header("Image Editing App 📸")
st.subheader("Upload an Image to get Started 🚀")

#Uploading image to web
image = st.file_uploader(label="Upload an image", type=['jpg','png'],accept_multiple_files=False)

# if image is uploaded
if image:
    # Getting image in PIL
    img = Image.open(image)
    # Adding sidebar
    st.sidebar.header("Editing panel")

    # writing setting code
    st.sidebar.write("Setting")
    setting_sharp = st.sidebar.slider("Sharpness")
    setting_color = st.sidebar.slider("Color")
    setting_brightness = st.sidebar.slider("Brightness")
    setting_contrast = st.sidebar.slider("Contrast")
    setting_blur = st.sidebar.slider("Blur")
    setting_flip_image = st.sidebar.selectbox(label="Flip Image",options=("Select Flip Direction","FLIP_TOP_BOTTOM","FLIP_LEFT_BOTTOM"))
    

    # Writing filter code
    filters = st.sidebar.selectbox("Filters",options=("None","Smooth","Detail","Emboss","Edge Enhance","B&W",))

    # resize image
    st.sidebar.write("Resize")
    new_width = st.sidebar.number_input(label="Width")
    new_height = st.sidebar.number_input(label="Height")
    submit = st.sidebar.button('Changes Size')

    st.sidebar.write("Resize by %")
    scale_percent = st.sidebar.number_input("Percent")
    submit1 = st.sidebar.button('Changes Scale Percent')

    st.sidebar.write("Rotate Image")
    rotate_image = st.sidebar.number_input("Degree")
    submit2 = st.sidebar.button("Rotate")

    # checking sharpness
    if setting_sharp:
        sharp_value = setting_sharp
    else:
        sharp_value = 0

    # checking color
    if setting_color:
        set_color = setting_color
    else:
        set_color = 1

    # checking brightness
    if setting_brightness:
        set_brightness = setting_brightness
    else:
        set_brightness = 1
    
    # checking contrast
    if setting_contrast:
        set_contrast = setting_contrast
    else:
        set_contrast = 1

    # checking blur
    if setting_blur:
        set_blur = setting_blur
    else:
        set_blur = 1


    # checking flip image
    flip_direction = setting_flip_image

    # implementing sharpness
    sharp = ImageEnhance.Sharpness(img)
    edited_img = sharp.enhance(sharp_value)

    # implementing colors
    color = ImageEnhance.Color(edited_img)
    edited_img = color.enhance(set_color)

    # implementing brightness
    brightness = ImageEnhance.Brightness(edited_img)
    edited_img = brightness.enhance(set_brightness)

    # implementing contrast
    contrast = ImageEnhance.Contrast(edited_img)
    edited_img = contrast.enhance(set_contrast)

    blur = edited_img.filter(GaussianBlur(set_blur))
    edited_img = blur

    if flip_direction == "FLIP_TOP_BOTTOM":
        edited_img = edited_img.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_direction == "FLIP_LEFT_RIGHT":
        edited_img = edited_img.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        pass

    filtered = edited_img
    if filters != "None":
        if filters == "Smooth":
            filtered = edited_img.filter(SMOOTH)
        elif filters == "Detail":
            filtered = edited_img.filter(DETAIL)
        elif filters == "Emboss":
            filtered = edited_img.filter(EMBOSS)
        elif filters == "Edge Enhance":
            fitered = edited_img.filter(EDGE_ENHANCE)
        elif filters == "B&W":
            filtered = edited_img.convert(mode='L')
    
    if submit:
        filtered = filtered.resize((new_height,new_width))

    if submit1:
        dimension = filtered.size
        width = int(dimension[0]* scale_percent / 100)
        height = int(dimension[1]* scale_percent / 100)
        filtered = filtered.resize((width, height))

    if submit2:
        filtered = filtered.rotate(rotate_image)
            
    
    col1, col2 = st.columns(2)
    col1.markdown("<h2>Original</h2>",unsafe_allow_html=True)
    col1.write(f"Size: {img.size}")
    col1.write(f"mode: {img.mode}")
    col1.image(image)
    col2.markdown("<h2>Result</h2>",unsafe_allow_html=True)
    col2.write(f"Size: {filtered.size}")
    col2.write(f"mode: {filtered.mode}")
    col2.image(filtered)
    st.write(">To download edited image right click and `click save image as`.")



