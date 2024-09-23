**Script de Análisis de Tráfico de Red**

## Resumen

Este script está diseñado para analizar el tráfico de red capturado en un archivo `.pcap` utilizando la biblioteca `pyshark`. Los resultados del análisis se exportan luego a un informe PDF utilizando la biblioteca `reportlab`.

## Características

- **Análisis de Paquetes**: El script analiza cada paquete en el archivo `.pcap` y extrae información relevante como las direcciones IP de origen y destino, los puertos TCP/UDP y las consultas DNS.
- **Generación de Informe PDF**: Los resultados del análisis se guardan en un informe PDF llamado `network_analysis_report.pdf` ubicado en el directorio `docs`.
- **Interfaz de Línea de Comandos**: Los usuarios pueden especificar el archivo `.pcap` a analizar a través de la línea de comandos. Si no se especifica ningún archivo, el script utiliza por defecto `data/network_capture.pcap`.

## Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- Biblioteca `pyshark`
- Biblioteca `reportlab`

Puedes instalar las bibliotecas requeridas utilizando pip:

```bash
pip install pyshark reportlab
```

## Estructura de Directorios

Asegúrate de que la estructura de directorios sea la siguiente:

```
Packet capture/
├── docs/
├── scripts/
│   ├── analyze_traffic.py
│   └── data/
│       └── network_capture.pcap
```

## Uso

### Ejecutar el Script

Para ejecutar el script, navega al directorio `scripts` y ejecuta:

```bash
python analyze_traffic.py
```

### Especificar un Archivo `.pcap` Diferente

Si deseas especificar un archivo `.pcap` diferente, puedes hacerlo pasando el nombre de archivo como argumento:

```bash
python analyze_traffic.py another_capture.pcap
```

Esto buscará `another_capture.pcap` en el directorio `data` y generará un informe PDF llamado `network_analysis_report.pdf` en el directorio `docs`.

### Salida

El script emitirá lo siguiente:

- Un mensaje que indica el archivo que se está analizando.
- Un mensaje que indica la finalización del análisis y el número de paquetes analizados.
- Un mensaje que indica la ubicación del informe PDF generado.

## Ejemplo de Salida

```bash
Analizando archivo: data/network_capture.pcap
Análisis de red completado. Se analizaron 500 paquetes. Informe guardado como docs/network_analysis_report.pdf
```

## Descripción del Código

### Función `analyze_packet`

Esta función analiza un solo paquete y extrae información relevante como:

- Número de paquete y capa más alta.
- Direcciones IP de origen y destino.
- Puertos TCP/UDP de origen y destino.
- Paquetes TCP SYN.
- Paquetes UDP grandes.
- Consultas DNS.

La información extraída se escribe luego en el informe PDF.

### Función `main`

Esta función coordina el proceso de análisis:

- Abre el archivo `.pcap` especificado utilizando `pyshark.FileCapture`.
- Inicializa el informe PDF y establece la fuente.
- Itera sobre cada paquete en el archivo de captura, llamando a `analyze_packet` para cada paquete.
- Guarda el informe PDF en el directorio `docs`.

### Interfaz de Línea de Comandos

El script admite argumentos de línea de comandos para especificar el archivo `.pcap` a analizar. Si no se especifica ningún archivo, se utiliza por defecto `data/network_capture.pcap`.

### Problemas de Dependencias

Si experimentas problemas con dependencias faltantes, asegúrate de que tanto `pyshark` como `reportlab` estén instalados. Puedes instalarlos utilizando pip como se describe en la sección de Requisitos Previos.

## Contribuciones

¡Siéntete libre de contribuir a este proyecto enviando pull requests o informando problemas! ¡Tus contribuciones son bienvenidas!

## Agradecimientos

- La biblioteca `pyshark` para el análisis de paquetes de red.
- La biblioteca `reportlab` para la generación de PDF.

---

# Network Traffic Analysis Script

## Overview

This script is designed to analyze network traffic captured in a `.pcap` file using the `pyshark` library. The analysis results are then exported to a PDF report using the `reportlab` library. 

## Features

- **Packet Analysis**: The script analyzes each packet in the `.pcap` file and extracts relevant information such as source and destination IP addresses, TCP/UDP ports, and DNS queries.
- **PDF Report Generation**: The analysis results are saved in a PDF report named `network_analysis_report.pdf` located in the `docs` directory.
- **Command-Line Interface**: Users can specify the `.pcap` file to analyze via the command line. If no file is specified, the script defaults to `data/network_capture.pcap`.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `pyshark` library
- `reportlab` library

You can install the required libraries using pip:

```bash
pip install pyshark reportlab
```

## Directory Structure

Ensure your directory structure looks like this:

```
Packet capture/
├── docs/
├── scripts/
│   ├── analyze_traffic.py
│   └── data/
│       └── network_capture.pcap
```

## Usage

### Running the Script

To run the script, navigate to the `scripts` directory and execute:

```bash
python analyze_traffic.py
```

### Specifying a Different `.pcap` File

If you want to specify a different `.pcap` file, you can do so by passing the filename as an argument:

```bash
python analyze_traffic.py another_capture.pcap
```

This will look for `another_capture.pcap` in the `data` directory and generate a PDF report named `network_analysis_report.pdf` in the `docs` directory.

### Output

The script will output the following:

- A message indicating the file being analyzed.
- A message indicating the completion of the analysis and the number of packets analyzed.
- A message indicating the location of the generated PDF report.

## Example Output

```bash
Analyzing file: data/network_capture.pcap
Network analysis completed. Analyzed 500 packets. Report saved as docs/network_analysis_report.pdf
```

## Code Overview

### `analyze_packet` Function

This function analyzes a single packet and extracts relevant information such as:

- Packet number and highest layer.
- Source and destination IP addresses.
- TCP/UDP source and destination ports.
- TCP SYN packets.
- Large UDP packets.
- DNS queries.

The extracted information is then written to the PDF report.

### `main` Function

This function orchestrates the analysis process:

- It opens the specified `.pcap` file using `pyshark.FileCapture`.
- It initializes the PDF report and sets the font.
- It iterates over each packet in the capture file, calling `analyze_packet` for each packet.
- It saves the PDF report to the `docs` directory.

### Command-Line Interface

The script supports command-line arguments to specify the `.pcap` file to analyze. If no file is specified, it defaults to `data/network_capture.pcap`.

### Dependency Issues

If you encounter issues with missing dependencies, ensure that both `pyshark` and `reportlab` are installed. You can install them using pip as described in the Prerequisites section.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues. Your contributions are welcome!

## Acknowledgments

- The `pyshark` library for network packet analysis.
- The `reportlab` library for PDF generation.

---
