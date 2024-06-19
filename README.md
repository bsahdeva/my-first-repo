# Polar Curves

This repository contains animations aiming to explain various attributes of polar curves, such as their nature, what equations look like what curves, differentiating polar curves, and finding area underneath polar curves.

## Animations

### First

TODO - Explaining what polar functions are and how they are different from traditional, cartesian functions

### Circles

#### Circles centered at the origin

$r(\theta) = a$

![](assets/CircleCurve_ManimCE_v0.18.1.png)

[pc_simple_circle.py](./pc_simple_circle.py)

#### Circle generated with $\cos(\theta)$

$r(\theta) = a \cdot \cos(\theta)$

![](assets/CosCircleCurve_ManimCE_v0.18.1.png)

[pc_cos_circle.py](./pc_cos_circle.py)

#### Circle generated with $\sin(\theta)$

$r(\theta) = a \cdot \sin(\theta)$

![](assets/SinCircleCurve_ManimCE_v0.18.1.png)

[pc_sin_circle.py](./pc_sin_circle.py)

### Limacons

$a + b \cdot \sin(\theta)$ and $a + b \cdot \cos(\theta)$

#### Looped Limacon

$|\frac{a}{b}| < 1$

![](assets/LoopedCurve_ManimCE_v0.18.1.png)

[looped.py](./looped.py)

#### Cardioid Limacon

$|\frac{a}{b}| = 1$

![](assets/CardioidCurve_ManimCE_v0.18.1.png)

[cardioid.py](./cardioid.py)

#### Dimpled Limacon

$|\frac{a}{b}| > 1$

![](assets/DimpledCurve_ManimCE_v0.18.1.png)

[dimpled.py](./dimpled.py)

### Rose Curves

$r(\theta) = a \cdot \sin(b \cdot \theta)$ and $r(\theta) = a \cdot \cos(b \cdot \theta)$

![](assets/RoseCurve_ManimCE_v0.18.1.png)

[rose_curves.py](./rose_curves.py)