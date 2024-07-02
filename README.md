# Progetto di Classificazione delle Immagini

Questo repository contiene il codice e i dati per il progetto di classificazione delle immagini. Il progetto utilizza vari modelli di deep learning per classificare immagini estratte da video. 

## Struttura delle Cartelle

- **dataset**: Contiene il dataset esportato da Roboflow.
- **strumenti utilizzati**: Contiene script Python sviluppati per estrarre frame da video.
- **notebook**: Contiene i notebook Jupyter per l'addestramento dei modelli e l'analisi dei risultati.

## Contenuto dei Notebook

- **MobileNetV2.ipynb**: Notebook per il training del modello MobileNetV2 e la visualizzazione dei grafici.
- **MobileNetV2Dataset2.ipynb**: Notebook per il training del modello MobileNetV2 su un dataset ridotto e con immagini extra.
- **densenet.ipynb**: Notebook per il training del modello DenseNet e la visualizzazione dei grafici.
- **demo.ipynb**: Notebook che permette di provare le funzionalità di classificazione dei tre modelli attraverso due modalità di funzionamento:
  1. Upload di un'immagine qualsiasi dal proprio PC.
  2. Inserimento di una parola attraverso una text bar. Il codice prenderà i segni corrispondenti e genererà un array di segni corrispondente alla parola, che verrà poi classificata utilizzando i tre modelli (DenseNet, MobileNet, VGG).

Per eseguire `demo.ipynb`, è sufficiente aprirlo e avviarlo su Google Colab, poiché i tre modelli sono salvati su Google Storage e vengono scaricati automaticamente.

