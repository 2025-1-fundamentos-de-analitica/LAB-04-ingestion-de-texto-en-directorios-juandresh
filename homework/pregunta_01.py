# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import zipfile
import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    zip = "files/input.zip"
    ruta = "files"
    ruta_zip ="files/input"

    if not os.path.exists(ruta):
        os.makedirs(ruta)
    
    if not os.path.exists(ruta_zip):
        with zipfile.ZipFile(zip, "r") as zip_ref:
            zip_ref.extractall(ruta)

    out_path = "files/output"

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    carpetas = ["negative", "neutral", "positive"]

#"files/input/test"
    phrases_test = []
    sentiments_test = []

    for em in carpetas:
        archivos = os.listdir("files/input/test/"+em)
        for file in archivos:
            with open(f"files/input/test/{em}/{file}", "r") as cont:
                phrases_test.append(cont.readline())
                sentiments_test.append(em)

    df_test = pd.DataFrame()
    df_test["phrase"] = phrases_test
    df_test["target"] = sentiments_test

    df_test.to_csv('files/output/test_dataset.csv', index=False)

#"files/input/train"
    phrases_train = []
    sentiments_train = []

    for em in carpetas:
        archivos = os.listdir("files/input/train/"+em)
        for file in archivos:
            with open(f"files/input/train/{em}/{file}", "r") as cont:
                phrases_train.append(cont.readline())
                sentiments_train.append(em)

    df_train = pd.DataFrame()
    df_train["phrase"] = phrases_train
    df_train["target"] = sentiments_train

    df_train.to_csv('files/output/train_dataset.csv', index=False)