# Reporte de otros dataset

Ejecutable: [`code/use_network`](https://github.com/StarBrand/CC5114-Tareas/blob/master/code/code/use_network.py)

## Dataset: `ecoli.data`

### Arquitectura SHORT

Argumentos: `-a short -x 3 -d ecoli -e 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_ecoli_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.6786 | 0.7895 | 0.9441 | 0.8599 |
| **im** |  | 0.5849 | 0.8017 | 0.6764 |
| **om** |  | nan | 0.0 | nan |
| **pp** |  | 0.0 | 0.0 | nan |

#### Undersampled

Argumentos: `-a short -x 3 -d ecoli -e 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_ecoli(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.56 | 0.6111 | 0.44 | 0.5116 |
| **im** |  | 0.7667 | 0.92 | 0.8364 |
| **om** |  | 0.3636 | 0.48 | 0.4138 |
| **pp** |  | 0.5263 | 0.4 | 0.4545 |

#### Oversampled

Argumentos: `-a short -x 3 -d ecoli -e 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_ecoli(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.7885 | 0.6882 | 0.8951 | 0.7781 |
| **im** |  | 0.8282 | 0.9441 | 0.8824 |
| **om** |  | 0.8871 | 0.7692 | 0.824 |
| **pp** |  | 0.7879 | 0.5455 | 0.6446 |

### Arquitectura LONG

Argumentos: `-a long -x 3 -d ecoli -e 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_ecoli_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.7679 | 0.7302 | 0.965 | 0.8313 |
| **im** |  | 0.8833 | 0.9138 | 0.8983 |
| **om** |  | nan | 0.0 | nan |
| **pp** |  | 0.5185 | 0.2692 | 0.3544 |

#### Undersampled

Argumentos: `-a long -x 3 -d ecoli -e 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_ecoli(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.62 | 0.6667 | 0.88 | 0.7586 |
| **im** |  | 0.7407 | 0.8 | 0.7692 |
| **om** |  | 0.5625 | 0.36 | 0.439 |
| **pp** |  | 0.4583 | 0.44 | 0.449 |

#### Oversampled

Argumentos: `-a long -x 3 -d ecoli -e 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_ecoli(oversampled)_3fold.png)

| Clases | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.6573 | 0.4615 | 0.4196 | 0.4396 |
| **im** |  | 0.9161 | 0.9161 | 0.9161 |
| **om** |  | 0.471 | 0.4545 | 0.4626 |
| **pp** |  | 0.7453 | 0.8392 | 0.7895 |

### Arquitectura BIG

Argumentos: `-a big -x 3 -d ecoli -e 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_ecoli_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.7887 | 0.8049 | 0.9231 | 0.8599 |
| **im** |  | 0.7937 | 0.8621 | 0.8264 |
| **om** |  | nan | 0.0 | nan |
| **pp** |  | 0.7174 | 0.6346 | 0.6735 |

#### Undersampled

Argumentos: `-a big -x 3 -d ecoli -e 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_ecoli(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.84 | 0.8333 | 0.8 | 0.8163 |
| **im** |  | 0.9231 | 0.96 | 0.9412 |
| **om** |  | 0.7692 | 0.8 | 0.7843 |
| **pp** |  | 0.8333 | 0.8 | 0.8163 |

#### Oversampled

Argumentos: `-a big -x 3 -d ecoli -e 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_ecoli(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **cp** | 0.8182 | 0.7143 | 0.8042 | 0.7566 |
| **im** |  | 0.8272 | 0.9371 | 0.8787 |
| **om** |  | 0.8673 | 0.6853 | 0.7656 |
| **pp** |  | 0.8897 | 0.8462 | 0.8674 |

## Dataset: `breast-cancer.data`

### Arquitectura SHORT

Argumentos: `-a short -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_breast-cancer_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.6958 | 0.7298 | 0.9005 | 0.8062 |
| **recurrence-events** |  | 0.4737 | 0.2118 | 0.2927 |

#### Undersampled

Argumentos: `-a short -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_breast-cancer(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.7294 | 0.6931 | 0.8235 | 0.7527 |
| **recurrence-events** |  | 0.7826 | 0.6353 | 0.7013 |

#### Oversampled

Argumentos: `-a short -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_breast-cancer(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.5199 | 0.5168 | 0.6119 | 0.5604 |
| **recurrence-events** |  | 0.5244 | 0.4279 | 0.4712 |

### Arquitectura LONG

Argumentos: `-a long -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_breast-cancer_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.7028 | 0.7479 | 0.8706 | 0.8046 |
| **recurrence-events** |  | 0.5 | 0.3059 | 0.3796 |

#### Undersampled

Argumentos: `-a long -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_breast-cancer(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.5706 | 0.5833 | 0.4941 | 0.535 |
| **recurrence-events** |  | 0.5612 | 0.6471 | 0.6011 |

#### Oversampled

Argumentos: `-a long -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_breast-cancer(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.4701 | 0.4483 | 0.2587 | 0.3281 |
| **recurrence-events** |  | 0.479 | 0.6816 | 0.5626 |

### Arquitectura BIG

Argumentos: `-a big -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_breast-cancer_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.6678 | 0.7345 | 0.8259 | 0.7775 |
| **recurrence-events** |  | 0.4167 | 0.2941 | 0.3448 |

#### Undersampled

Argumentos: `-a big -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_breast-cancer(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.5765 | 0.567 | 0.6471 | 0.6044 |
| **recurrence-events** |  | 0.589 | 0.5059 | 0.5443 |

#### Oversampled

Argumentos: `-a big -x 3 -d breast_cancer -l 0 -c 0 1 2 3 4 5 6 7 8 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_breast-cancer(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **no-recurrence-events** | 0.7338 | 0.7582 | 0.6866 | 0.7206 |
| **recurrence-events** |  | 0.7136 | 0.7811 | 0.7458 |

## Dataset: `Data_for_UCI_named.csv`

### Arquitectura SHORT

Argumentos: `-a short -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_uci_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.6775 | 0.7217 | 0.1776 | 0.2851 |
| **unstable** |  | 0.6732 | 0.9611 | 0.7918 |

##### Entrada normalizada

Argumentos: `-a short -n -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_normalized_on_uci_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.7107     | 0.712       | 0.3373   | 0.4577     |
| **unstable** |            | 0.7104      | 0.9226   | 0.8027     |

#### Undersampled

Argumentos: `-a short -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_uci(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.6308 | 0.6959 | 0.4646 | 0.5572 |
| **unstable** |  | 0.5982 | 0.797 | 0.6834 |

##### Entrada normalizada

Argumentos: `-a short -n -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_normalized_on_uci(undersampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.7138     | 0.7151      | 0.7108   | 0.7129     |
| **unstable** |            | 0.7125      | 0.7169   | 0.7147     |

#### Oversampled

Argumentos: `-a short -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_network_on_uci(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.5047 | 0.9839 | 0.0096 | 0.0189 |
| **unstable** |  | 0.5024 | 0.9998 | 0.6687 |

##### Entrada normalizada

Argumentos: `-a short -n -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/short_normalized_on_uci(oversampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.6216     | 0.665       | 0.49     | 0.5642     |
| **unstable** |            | 0.5962      | 0.7531   | 0.6656     |

### Arquitectura LONG

Argumentos: `-a long -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_uci_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.7452 | 0.6861 | 0.5459 | 0.608 |
| **unstable** |  | 0.7691 | 0.8583 | 0.8113 |

##### Entrada normalizada

Argumentos: `-a long -n -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_normalized_on_uci_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.8369     | 0.9209      | 0.6011   | 0.7274     |
| **unstable** |            | 0.8109      | 0.9707   | 0.8836     |

#### Undersampled

Argumentos: `-a long -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_network_on_uci(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.6981 | 0.7016 | 0.6892 | 0.6954 |
| **unstable** |  | 0.6946 | 0.7069 | 0.7007 |

##### Entrada normalizada

Argumentos: `-a long -n -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/long_normalized_on_uci(undersampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.8802     | 0.8447      | 0.9318   | 0.8861     |
| **unstable** |            | 0.9239      | 0.8287   | 0.8737     |

#### Oversampled

Argumentos: `-a long -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_uci(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.5352 | 0.8615 | 0.0839 | 0.1528 |
| **unstable** |  | 0.5185 | 0.9865 | 0.6797 |

##### Entrada normalizada

Argumentos: `-a long -n -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_normalized_on_uci(oversampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.8166     | 0.8135      | 0.8216   | 0.8175     |
| **unstable** |            | 0.8198      | 0.8116   | 0.8157     |

### Arquitectura BIG

Argumentos: `-a big -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_uci_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.7064 | 0.6825 | 0.3533 | 0.4656 |
| **unstable** |  | 0.7119 | 0.9067 | 0.7976 |

##### Entrada normalizada

Argumentos: `-a big -n -x 3 -d uci -H 0`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_normalized_on_uci_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.8871     | 0.8419      | 0.8472   | 0.8446     |
| **unstable** |            | 0.913       | 0.9097   | 0.9114     |

#### Undersampled

Argumentos: `-a big -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_uci(undersampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.7262 | 0.7188 | 0.7434 | 0.7309 |
| **unstable** |  | 0.7343 | 0.7091 | 0.7215 |

##### Entrada normalizada

Argumentos: `-a big -n -x 3 -d uci -H 0 -u`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_normalized_on_uci(undersampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.9054     | 0.8912      | 0.9235   | 0.9071     |
| **unstable** |            | 0.9206      | 0.8873   | 0.9036     |

#### Oversampled

Argumentos: `-a big -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_network_on_uci(oversampled)_3fold.png)

| Clases	| *Accuracy* | *Precision* | *Recall* | *f1-score* |
| --------------- | ---------- | ----------- | -------- | ---------- |
| **stable** | 0.7375 | 0.7511 | 0.7105 | 0.7302 |
| **unstable** |  | 0.7254 | 0.7646 | 0.7444 |

##### Entrada normalizada

Argumentos: `-a big -n -x 3 -d uci -H 0 -o`

![](https://github.com/StarBrand/CC5114-Tareas/blob/master/tarea1/results/other_dataset/big_normalized_on_uci(oversampled)_3fold.png)

| Clases       | *Accuracy* | *Precision* | *Recall* | *f1-score* |
| ------------ | ---------- | ----------- | -------- | ---------- |
| **stable**   | 0.9341     | 0.9233      | 0.9469   | 0.9349     |
| **unstable** |            | 0.9455      | 0.9213   | 0.9332     |
