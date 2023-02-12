% Secure Software Design
% Andey Robins
% Spring 23 - Supplemental 1

# An In-depth Look at RSA

## Outline

- Foundations
  - Groups
- RSA Function
- Key Generation
- Takeaways

---

![Similar to in class crypto, we source information from this book](./ssd/assets/05/serious-crypto.png)

# Groups

## What's in a Group

A set with elements obeying these axioms:

- **Closure:** For any two _x_ and _y_ in a group, _x * y_ is also in the group
- **Associativity:** For any _x, y, z_ in a group, _(x * y) * z = x * (y * z)_
- **Identity Existence:** There's some element _i_ such that _i * x = x * i = x_
- **Inverse Existence:** For any _x_ in a group, there is some _y_ such that _x * y = y * x = i_

## Other Properties of Groups

Outside of the axioms, these are useful features of many groups.

- **Commutative:** _x * y = y * x_
- **Cyclic:** There is some element _g_ such that _g^1, g^2, g^3, etc._ span all distinct elements.
- **Generator:** If the group is cyclic, the element _g_ is called the generator.

## Group Proof Exercise

As an excercise to the student, show this is true. **Z** is the integers and the subscript 4 indicates our group is the integers modulo 4.

$$ \mathbb{Z}_4^* = \{1, 3\} $$

Two is not coprime with 4, which is the intuition behind why it is not within the group. Further, what is the generator for this group?

# RSA Function

## RSA Encoding

RSA encodes a message as a single, positive integer between 1 and _n_ - 1 where _n_ is a large number called the _modulus_. More specifically, it works on all the numbers less than _n_ which are coprime with _n_ (no common prime factors). These numbers form the group:

$$ \mathbb{Z}_n^* $$

## Encryption with RSA

$$ \text{Let } x \text{ be the number to be encrypted which belongs to } \mathbb{Z}_n^* \text{.} $$ 
$$ \text{Then, RSA encrypts this number as } y = x^e \text{ mod } n $$

Or the encrypted message multiplied by itself _e_ times modulus _n_. _e_ and _n_ thus make up the public key.

## Decryption with RSA

Let us denote the "private key" as _d_.

$$ y^d \text{ mod } n = (x^e)^d \text{ mod } n = x^{ed} \text{ mod } n = x $$

Since we select _d_ to be the inverse of _e_, _ed = 1_.

## Euler's Totient Function

This function gives the number of elements coprime with _n_. If _n_ is the product of prime numbers:

$$ \phi(n) = (p_1 - 1) \times (p_2 - 1) \times ... \times (p_m - 1) $$

Since RSA operates with large prime numbers such that _n = pq_,

$$ \phi(n) = (p-1)(q-1) = | \mathbb{Z}_n^* | $$

---

This is important, because our choices for _ed = 1_ is all mod _phi(n)_.

Therefore, if you can compute _phi(n)_, you can break any RSA encryption since d can be derived from _phi(n)_ and _e_.

**So where do the _p_ and _q_ that define _phi(n)_ come from?**

# Key Generation

## Generating Keys for RSA

1. Pick two large prime numbers _p_ and _q_
2. Calculate _n_ as _pq_
3. Calculate _phi(n)_ as _(p-1)(q-1)_
4. Pick a random prime number less than _phi_ to be _e_
5. Calculate the value _d_ from _phi_ and _e_
6. Share _n_ and _e_ as the public key

## Assumptions

1. Factoring is a hard problem
2. Calculating _e_ -th roots is a hard problem
    - This is an assertion that appears to derive from the study of rings, something I mention but have no further ability to comment on.

_"These seem closely connected, though we don't know for sure whether they are equivalent."_ - Jean-Phillipe Aumasson

## Takeaways

1. If using RSA, ensure your generation of _p_ and _q_ are done in secure ways since the entire system relies on their secrecy.
2. Pick large numbers for _p_ and _q_ (standard is to look for numbers which yield an _n_ with 4096 bits).
3. _p_ and _q_ should be unrelated, random primes of similar size that are not too close in value.