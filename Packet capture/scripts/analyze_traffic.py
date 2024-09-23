import pyshark
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def analyze_packet(packet, pdf, y_position):
    packet_info = f"Packet {packet.number}: {packet.highest_layer}\n"
    
    if 'IP' in packet:
        packet_info += f"  Source IP: {packet.ip.src}\n"
        packet_info += f"  Destination IP: {packet.ip.dst}\n"
    
    if 'TCP' in packet:
        packet_info += f"  TCP - Source Port: {packet.tcp.srcport}, Destination Port: {packet.tcp.dstport}\n"
        if packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '0':
            packet_info += "  TCP SYN packet detected\n"
    
    elif 'UDP' in packet:
        packet_info += f"  UDP - Source Port: {packet.udp.srcport}, Destination Port: {packet.udp.dstport}\n"
        if int(packet.udp.length) > 1000:
            packet_info += "  Large UDP packet detected\n"
    
    elif 'DNS' in packet:
        if hasattr(packet.dns, 'qry_name'):
            packet_info += f"  DNS query: {packet.dns.qry_name}\n"
    
    packet_info += "\n"  # Empty line for readability
    pdf.drawString(100, y_position, packet_info)
    y_position -= 100  # Adjust this value to control the spacing between lines
    if y_position < 100:  # Check if we need a new page
        pdf.showPage()
        y_position = 750  # Reset y_position for the new page
    return y_position

def main(pcap_file):
    print(f"Analyzing file: {pcap_file}")
    
    cap = pyshark.FileCapture(pcap_file)

    packet_count = 0
    pdf_path = os.path.join('docs', 'network_analysis_report.pdf')
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    pdf.setFont("Helvetica", 12)
    y_position = 750  # Start at the top of the page

    for packet in cap:
        packet_count += 1
        y_position = analyze_packet(packet, pdf, y_position)

    pdf.save()
    print(f"Network analysis completed. Analyzed {packet_count} packets. Report saved as {pdf_path}")

if __name__ == "__main__":
    default_file = os.path.join('data', 'network_capture.pcap')
    
    if len(sys.argv) > 1:
        pcap_file = os.path.join('data', sys.argv[1])
    else:
        pcap_file = default_file

    if not os.path.exists(pcap_file):
        print(f"Error: The file '{pcap_file}' does not exist.")
        print("Available capture files:")
        for file in os.listdir('data'):
            if file.endswith('.pcap'):
                print(f"  - {file}")
        sys.exit(1)
    
    main(pcap_file)