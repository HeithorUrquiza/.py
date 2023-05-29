import * as tf from '@tensorflow/tfjs';

// Dados de treinamento e teste
const trainData = ...; // Dados de treinamento (características das transações)
const trainLabels = ...; // Rótulos de treinamento (indicando se cada transação é fraudulenta ou não)
const testData = ...; // Dados de teste (características das transações)
const testLabels = ...; // Rótulos de teste (indicando se cada transação é fraudulenta ou não)

// Criação do modelo
const model = tf.sequential();
model.add(tf.layers.dense({ units: 16, activation: 'relu', inputShape: [trainData.shape[1]] }));
model.add(tf.layers.dense({ units: 1, activation: 'sigmoid' }));

// Compilação do modelo
model.compile({ optimizer: 'adam', loss: 'binaryCrossentropy' });

// Treinamento do modelo
await model.fit(trainData, trainLabels, { epochs: 10 });

// Predições no conjunto de teste
const predictions = model.predict(testData) as tf.Tensor;

// Obtenção das probabilidades de classe positiva (fraude)
const probabilities = predictions.dataSync();

// Cálculo das métricas Precision e Recall para diferentes limiares
const thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]; // Valores de limiar
const precisionValues: number[] = [];
const recallValues: number[] = [];

for (const threshold of thresholds) {
  let truePositives = 0;
  let falsePositives = 0;
  let falseNegatives = 0;

  for (let i = 0; i < probabilities.length; i++) {
    const predictedLabel = probabilities[i] >= threshold ? 1 : 0;
    const trueLabel = testLabels[i];

    if (predictedLabel === 1 && trueLabel === 1) {
      truePositives++;
    } else if (predictedLabel === 1 && trueLabel === 0) {
      falsePositives++;
    } else if (predictedLabel === 0 && trueLabel === 1) {
      falseNegatives++;
    }
  }

  const precision = truePositives / (truePositives + falsePositives);
  const recall = truePositives / (truePositives + falseNegatives);

  precisionValues.push(precision);
  recallValues.push(recall);
}

// Plotagem da curva Precision-Recall
import * as plotly from 'plotly.js';

const data = [
  {
    x: recallValues,
    y: precisionValues,
    type: 'scatter',
    mode: 'lines',
  },
];

const layout = {
  title: 'Curva Precision-Recall',
  xaxis: {
    title: 'Recall',
  },
  yaxis: {
    title: 'Precision',
  },
};

plotly.plot(data, layout);
