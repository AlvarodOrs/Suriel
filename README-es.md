# Suriel

Predicción financiera con incertidumbre mediante Redes Neuronales Bayesianas para modelado probabilístico de series temporales y análisis de decisiones sensibles al riesgo.

---

## Descripción general

Suriel es un framework de investigación modular para evaluar métodos de deep learning probabilístico aplicados a la predicción de series temporales financieras. El foco no está en la predicción puntual del precio, sino en la calidad, calibración y utilidad de la incertidumbre bajo condiciones de mercado no estacionarias.

Los sistemas tradicionales de forecasting producen valores deterministas. Suriel, en cambio, modela distribuciones predictivas completas, permitiendo representar explícitamente la incertidumbre epistémica y su relación con el riesgo financiero, los cambios de régimen y la degradación del modelo.

Pregunta central de investigación:

> ¿Proporcionan las Redes Neuronales Bayesianas estimaciones de incertidumbre mejor calibradas que los modelos deterministas y ensembles, y se traduce esto en mejores decisiones bajo riesgo en entornos financieros realistas?

El sistema está diseñado como una tubería experimental para el benchmarking de machine learning probabilístico en finanzas.

---

## Objetivos

- Desarrollar un framework reproducible para predicción financiera probabilística
- Comparar Redes Neuronales Bayesianas frente a modelos deterministas y ensembles
- Evaluar la calibración de la incertidumbre en distintos regímenes de mercado
- Analizar la relación entre incertidumbre y error de predicción
- Estudiar si la incertidumbre mejora decisiones simuladas bajo gestión de riesgo
- Proporcionar un entorno reproducible de experimentación y benchmarking

---

## Alcance

### Capa de datos
- Series temporales financieras históricas (configurables por activos)
- Preprocesado y feature engineering consistente en el tiempo
- Separación estricta temporal (train / validación / test) para evitar fuga de información

### Capa de modelos

**Modelos deterministas:**
- Redes MLP lineales y no lineales
- Arquitecturas LSTM / GRU
- Transformers para series temporales (extensión opcional)
- Baselines estadísticos clásicos (ARIMA, GARCH cuando aplique)

**Modelos probabilísticos:**
- Redes Neuronales Bayesianas (inferencia variacional)
- Monte Carlo Dropout
- Ensembles profundos como baseline probabilístico

---

## Modelado de incertidumbre

- Estimación de distribuciones predictivas en lugar de predicciones puntuales
- Separación de componentes de incertidumbre:
  - Incertidumbre epistémica (modelo)
  - Incertidumbre aleatoria (ruido de datos)
- Análisis de calibración de probabilidades predictivas

---

## Framework de evaluación

**Rendimiento predictivo:**
- MAE / RMSE

**Rendimiento probabilístico:**
- Log-likelihood negativo (NLL)
- CRPS (Continuous Ranked Probability Score)

**Calibración:**
- Error de calibración esperado (ECE)
- Diagramas de fiabilidad

**Métricas financieras simuladas:**
- Ratio de Sharpe (estrategias simuladas)
- Máximo drawdown
- Sensibilidad a costes de transacción
- Estabilidad del retorno ajustado al riesgo en distintos regímenes

---

## Arquitectura del sistema

Suriel está estructurado como una pipeline modular de investigación:

1. **Pipeline de datos**
   - ingesta, limpieza, normalización, generación de variables

2. **Capa de entrenamiento**
   - entrenamiento de modelos deterministas y probabilísticos

3. **Capa de inferencia**
   - generación de distribuciones predictivas e incertidumbre

4. **Motor de evaluación**
   - benchmarking estadístico y financiero

5. **Simulador de backtesting**
   - simulación de cartera basada en datos históricos

---

## Restricciones

- No incluye trading en tiempo real ni conexión a brokers
- No asume estacionariedad en las series financieras
- Toda evaluación es temporalmente consistente (sin leakage)
- El backtesting incluye costes de transacción y slippage
- Diseñado para investigación, no para producción financiera

---

## Roadmap

Suriel sigue un pipeline de validación por fases basado en evidencia estadística. El avance entre fases depende de resultados empíricos, no de progreso de implementación.

---

### Fase 0: Diseño de investigación y especificación experimental

Definición del framework antes de implementar modelos.

**Entregables:**
- Definición formal del problema (target, horizonte, activos)
- Especificación de datasets y fuentes
- Diseño de partición temporal (train / validación / test)
- Definición de modelos baseline
- Definición de modelos probabilísticos
- Definición de métricas de evaluación
- Supuestos del backtesting (costes, slippage, restricciones)

**Criterio de salida:**
- Protocolo experimental completamente reproducible antes del entrenamiento

---

### Fase 1: Implementación y entrenamiento de modelos

Implementación de modelos deterministas y probabilísticos.

**Entregables:**
- Pipeline modular de ML
- Modelos baseline entrenados
- Modelos Bayesianos y ensembles implementados
- Feature engineering
- Evaluación inicial offline

**Criterio de salida:**
- Baselines estables y reproducibles
- Salidas probabilísticas coherentes

---

### Fase 2: Backtesting histórico y validación estadística

#### Fase 2.0: Backtesting offline

Evaluación completa sobre datos históricos no vistos.

**Entregables:**
- Validación walk-forward
- Backtesting con ventanas deslizantes
- Simulación de costes de transacción
- Análisis por regímenes de mercado (volatilidad, crisis, mercados alcistas/bajistas)
- Diagnóstico de calibración por régimen

**Criterio de salida:**
- Evidencia de calibración y estabilidad en distintos regímenes
- Ausencia de leakage u overfitting

---

#### Fase 2.1: Simulación en vivo (paper trading)

Ejecución en tiempo real sin exposición de capital.

**Entregables:**
- Ingesta de datos en tiempo real
- Sistema de paper trading
- Monitorización de drift y latencia
- Seguimiento de rendimiento en condiciones reales

**Criterio de salida:**
- Estabilidad en simulación prolongada
- Consistencia con backtesting

---

### Fase 3: Validación en entorno real controlado (solo capital propio)

#### Fase 3.0: Despliegue mínimo de capital

Pruebas en mercado real con restricciones estrictas.

**Restricciones:**
- Límites fijos de riesgo
- Exposición controlada
- Sin apalancamiento (o estrictamente limitado)
- Registro completo de decisiones

**Entregables:**
- Sistema de seguimiento de ejecución
- Comparación entre resultados simulados y reales
- Análisis de impacto de ejecución y slippage

**Criterio de salida:**
- Consistencia estadística entre simulación y realidad

---

#### Fase 3.1: Ampliación de capital propio

Incremento progresivo solo tras validación previa.

**Entregables:**
- Evaluación multi-activo
- Estrés en escenarios de volatilidad extrema
- Ajuste de asignación de riesgo

**Criterio de salida:**
- Estabilidad en múltiples periodos de mercado

---

### Fase 4: Publicación e सहयोग externo

Solo tras validación completa y reproducibilidad.

**Requisitos:**
- Informes auditables
- Reproducibilidad total del sistema
- Validación externa del enfoque

**Entregables:**
- Paper técnico o informe de investigación
- Framework open-source (opcional)
- Propuestas de colaboración

---

### Fase 5: Producción (opcional)

Solo si los resultados justifican despliegue.

**Entregables:**
- API de inferencia
- Sistema de monitorización y drift detection
- Pipeline de reentrenamiento
- Control de versiones de modelos

---

## No objetivos

- Sistemas de trading de alta frecuencia
- Garantía de rentabilidad o generación de alpha
- Captación de capital externo no regulado
- Escalado de capital sin validación estadística
- Resultados no reproducibles

---

## Estado actual

Fase activa de investigación e implementación.

Enfoque actual:
- implementación de baselines
- desarrollo del pipeline probabilístico
- construcción del framework de backtesting
- métricas de calibración y evaluación