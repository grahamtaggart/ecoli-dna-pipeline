import streamlit as st
from Bio import SeqIO
import matplotlib.pyplot as plt

def read_genbank_file(file_content):
    records = list(SeqIO.parse(file_content, "genbank"))
    return records

def display_sequence_info(record):
    st.subheader("Sequence Information")
    st.write(f"ID: {record.id}")
    st.write(f"Description: {record.description}")
    st.write(f"Length: {len(record)} bp")
    st.write(f"Features: {len(record.features)}")

def plot_gc_content(record):
    gc_percentages = [(feature.location.start, feature.location.end, feature.location.strand, feature.qualifiers.get('GC_percent', [0])[0]) for feature in record.features if 'GC_percent' in feature.qualifiers]
    
    if not gc_percentages:
        st.warning("No GC content information found in features.")
        return

    st.subheader("GC Content Plot")
    fig, ax = plt.subplots()
    for start, end, strand, gc_percent in gc_percentages:
        ax.plot([start, end], [gc_percent, gc_percent], label=f"Strand: {strand}")

    ax.set_xlabel("Position")
    ax.set_ylabel("GC Content (%)")
    ax.set_title("GC Content along the Sequence")
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title("Genomic Data Visualization with Streamlit and BioPython")

    uploaded_file = st.file_uploader("Upload a GenBank file", type=["gb", "gbk"])
    
    if uploaded_file is not None:
        records = read_genbank_file(uploaded_file)

        if not records:
            st.error("No records found in the GenBank file.")
        else:
            selected_record = st.selectbox("Select a record", records)
            display_sequence_info(selected_record)
            plot_gc_content(selected_record)

if __name__ == "__main__":
    main()

