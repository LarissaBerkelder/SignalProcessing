# Notch filter

## Normalized Frequency

$$\omega_n = \frac{2\pi f_{\text{interference}}}{f_s} $$

Where $f_{\text{interference}}$ is 6000 Hz and ${f_s}$ is 16,000 Hz. 

$$ \omega_n = \frac{2\pi * 6000}{16000} $$

```python
normalized_freq = (2*np.pi * f_interference) / sample_rate
```
The normalized frequency is: 2.356194490192345

## Deriving the Difference Equation

The transfer function of the notch filter is:
$$
H(z) = \frac{1 - 2\cos(\omega_n)z^{-1} + z^{-2}}{1 - 2a\cos(\omega_n)z^{-1} + a^2z^{-2}}
$$

Numerator
$$1-2\cos(\omega_n) z^{-1}+z^{-2}$$
Denomenator
$$1-2a\cos(\omega_n) z^{-1}+a^2z^{-2} $$

This relates the input \(X(z)\) and output \(Y(z)\) in the z-domain:
$$H(z) = \frac{Y(z)}{X(z)} $$
Rewriting:
$$
Y(z) = H(z) \cdot X(z)
$$

Substitute \(H(z)\):
$$
Y(z) = \frac{1 - 2\cos(\omega_n)z^{-1} + z^{-2}}{1 - 2a\cos(\omega_n)z^{-1} + a^2z^{-2}} * X(z) $$
Multiply through by the denominator:
$$
(1 - 2a\cos(\omega_n)z^{-1} + a^2z^{-2}) Y(z) =
(1 - 2\cos(\omega_n)z^{-1} + z^{-2}) X(z)
$$

Left side
$$
(1 - 2a\cos(\omega_n)z^{-1} + a^2z^{-2}) Y(z) \\
Y(z) - 2a\cos(\omega_n) z^{-1} Y(z) +a^2z^{-2} Y(z)
$$
In time domain
$$
Y[n] - 2a\cos(\omega_n) Y[n-1] a^2 Y[n-2] 
$$

Right side
$$
(1 - 2\cos(\omega_n)z^{-1} + z^{-2}) X(z) \\
X(z) - 2\cos(\omega_n)z^{-1} X(z) + z^{-2} X(z)
$$
In time domain
$$
X[n]- 2\cos(\omega_n) X[n-1] + X[n-2]
$$

Combining
$$
Y[n] - 2a\cos(\omega_n) Y[n-1] + a^2 Y[n-2] = X[n] - 2\cos(\omega_n) X[n-1] + X[n-2]
$$

Final Difference Equation
$$
Y[n] = 2a\cos(\omega_n) Y[n-1] - a^2 Y[n-2] + X[n]- 2\cos(\omega_n) X[n-1] + X[n-2]
$$