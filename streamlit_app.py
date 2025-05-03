import streamlit as st

# Set page config must be the very first Streamlit command
st.set_page_config(
    page_title="PDF Obfuscation Tool",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
import tempfile
from app import (
    convert_pdf_to_images,
    apply_unicode_obfuscation,
    inject_invisible_text,
    apply_copy_protection,
    apply_text_layer_manipulation,
    apply_dynamic_watermark,
    apply_character_spacing_manipulation,
    apply_micro_text_patterns,
    apply_font_substitution,
    apply_text_path_manipulation,
    apply_content_scrambling,
    apply_pattern_obfuscation,
    apply_metadata_manipulation,
    apply_hybrid_protection,
    apply_prompt_injection
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin: 0.5rem 0;
    }
    .stDownloadButton>button {
        width: 100%;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("PDF Obfuscation Tool")
st.write("Upload a PDF and apply various obfuscation techniques to make it harder to copy or extract text.")

# Create a temporary directory for uploaded files
temp_dir = tempfile.mkdtemp()

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File uploaded successfully: {uploaded_file.name}")
    
    # Display options for obfuscation techniques
    st.subheader("Select Obfuscation Techniques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Techniques")
        image_based = st.checkbox("Convert to Image-based PDF", 
                                help="Converts text to images, making it non-selectable")
        unicode_obfuscation = st.checkbox("Apply Unicode Obfuscation", 
                                        help="Replace characters with similar-looking Unicode characters")
        text_layers = st.checkbox("Apply Text Layer Manipulation",
                                help="Adds multiple overlapping text layers to confuse extraction")
        dynamic_watermark = st.checkbox("Apply Dynamic Watermark",
                                      help="Adds changing watermarks to each page")
        font_substitution = st.checkbox("Apply Font Substitution",
                                      help="Uses similar-looking fonts with different character mappings")
        text_path = st.checkbox("Apply Text Path Manipulation",
                              help="Converts text to paths with subtle distortions")
    
    with col2:
        st.markdown("### Advanced Techniques")
        invisible_text = st.checkbox("Inject Invisible Text", 
                                    help="Add hidden text to confuse extraction tools")
        copy_protection = st.checkbox("Apply Copy Protection", 
                                    help="Set PDF permissions to disable copying")
        character_spacing = st.checkbox("Apply Character Spacing",
                                      help="Randomly adjusts spacing between characters")
        micro_patterns = st.checkbox("Apply Micro Text Patterns",
                                   help="Adds tiny patterns and zero-width characters")
        content_scrambling = st.checkbox("Apply Content Scrambling",
                                       help="Scrambles content order while maintaining appearance")
        pattern_obfuscation = st.checkbox("Apply Pattern Obfuscation",
                                        help="Adds complex background patterns")
        metadata_manipulation = st.checkbox("Apply Metadata Manipulation",
                                          help="Adds misleading document information")
    
    # Protection options
    st.subheader("Protection Options")
    protection_type = st.radio(
        "Choose protection type:",
        ["Hybrid Protection (All Techniques)", "Prompt Injection Only"]
    )
    
    # Process button
    if st.button("Process PDF", type="primary"):
        results = {}
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Calculate total steps (including hybrid protection if selected)
        techniques_selected = sum([
            image_based, unicode_obfuscation, invisible_text, 
            copy_protection, text_layers, dynamic_watermark,
            character_spacing, micro_patterns, font_substitution,
            text_path, content_scrambling, pattern_obfuscation,
            metadata_manipulation
        ])
        if protection_type == "Hybrid Protection (All Techniques)":
            techniques_selected += 1
        
        if techniques_selected == 0:
            st.warning("Please select at least one obfuscation technique.")
        else:
            progress_step = 1.0 / techniques_selected
            progress_value = 0.0
            
            # Process each selected technique
            if image_based:
                status_text.text("Converting PDF to images...")
                results["image_based"] = convert_pdf_to_images(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if unicode_obfuscation:
                status_text.text("Applying Unicode obfuscation...")
                results["unicode_obfuscation"] = apply_unicode_obfuscation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if text_layers:
                status_text.text("Applying text layer manipulation...")
                results["text_layers"] = apply_text_layer_manipulation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if dynamic_watermark:
                status_text.text("Applying dynamic watermark...")
                results["dynamic_watermark"] = apply_dynamic_watermark(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if character_spacing:
                status_text.text("Applying character spacing manipulation...")
                results["character_spacing"] = apply_character_spacing_manipulation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if micro_patterns:
                status_text.text("Applying micro text patterns...")
                results["micro_text_patterns"] = apply_micro_text_patterns(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if font_substitution:
                status_text.text("Applying font substitution...")
                results["font_substitution"] = apply_font_substitution(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if text_path:
                status_text.text("Applying text path manipulation...")
                results["text_path"] = apply_text_path_manipulation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if content_scrambling:
                status_text.text("Applying content scrambling...")
                results["content_scrambling"] = apply_content_scrambling(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if pattern_obfuscation:
                status_text.text("Applying pattern obfuscation...")
                results["pattern_obfuscation"] = apply_pattern_obfuscation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if metadata_manipulation:
                status_text.text("Applying metadata manipulation...")
                results["metadata_manipulation"] = apply_metadata_manipulation(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if invisible_text:
                status_text.text("Injecting invisible text...")
                results["invisible_text"] = inject_invisible_text(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if copy_protection:
                status_text.text("Applying copy protection...")
                results["copy_protection"] = apply_copy_protection(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            if protection_type == "Hybrid Protection (All Techniques)":
                status_text.text("Applying hybrid protection...")
                results["hybrid_protection"] = apply_hybrid_protection(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            else:
                status_text.text("Applying prompt injection...")
                results["prompt_injection"] = apply_prompt_injection(temp_file_path)
                progress_value += progress_step
                progress_bar.progress(progress_value)
            
            progress_bar.progress(1.0)
            status_text.text("Processing complete!")
            
            # Display download links
            st.subheader("Download Processed Files")
            
            if results:
                # Group download buttons in columns
                cols = st.columns(2)
                for i, (technique, file_path) in enumerate(results.items()):
                    with open(file_path, "rb") as file:
                        file_name = os.path.basename(file_path)
                        technique_name = technique.replace("_", " ").title()
                        cols[i % 2].download_button(
                            label=f"Download {technique_name} PDF",
                            data=file,
                            file_name=file_name,
                            mime="application/pdf"
                        )
            else:
                st.warning("No obfuscation techniques were selected.")

# Sidebar content
with st.sidebar:
    st.title("About")
    st.markdown("""
    This tool allows you to obfuscate PDF documents using various techniques to 
    protect content from easy copying or extraction.
    
    ### Available Techniques:
    
    **Basic Techniques:**
    1. **Image-based PDF**: Converts text to images
    2. **Unicode Obfuscation**: Uses visually similar characters
    3. **Text Layer Manipulation**: Adds overlapping text layers
    4. **Dynamic Watermark**: Adds changing watermarks per page
    5. **Font Substitution**: Uses similar-looking fonts
    6. **Text Path Manipulation**: Converts text to paths
    
    **Advanced Techniques:**
    7. **Invisible Text**: Adds hidden text to confuse extraction
    8. **Copy Protection**: Sets PDF permissions
    9. **Character Spacing**: Randomly adjusts spacing
    10. **Micro Text Patterns**: Adds tiny patterns
    11. **Content Scrambling**: Reorders content
    12. **Pattern Obfuscation**: Adds background patterns
    13. **Metadata Manipulation**: Adds misleading info
    
    **Combined Protection:**
    14. **Hybrid Protection**: Combines multiple techniques
    15. **Prompt Injection**: Adds invisible prompts to disrupt AI processing
    """)