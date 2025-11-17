# Multi-Armed Bandit: Thompson Sampling & UCB1

This project contains two algorithms used to solve the **Multi-Armed Bandit problem**:  
**Thompson Sampling** and **UCB1 (Upper Confidence Bound)**.  
Both algorithms are implemented using the same dataset, and the goal is to understand how each method learns to choose the best option over time.

---

## 🎯 Problem Description: Multi-Armed Bandit

The Multi-Armed Bandit problem represents a situation where you have several choices (called "arms"), and each choice gives a reward with an unknown probability.

Example:
You have **10 ads**, and each ad gets a “click” with a different unknown probability.  
Your mission:

> "Maximize total clicks by deciding which ad to show each time."

The challenge is balancing:
- **Exploration**: trying different ads to learn about them  
- **Exploitation**: choosing the ads that already look good  

This is the core idea behind many real-world systems:
- Online advertising  
- Recommendation systems  
- A/B testing  
- Medicine/drug trials  
- Game AI  

---

## 🧠 Algorithm 1: Thompson Sampling

**Idea**:  
Use probability and Bayesian thinking to estimate how “good” each ad is, and choose based on random samples from these estimates.

**How it works**:
1. For each ad, keep:
   - number of successes (clicks)
   - number of failures (no click)

2. Represent each ad with a **Beta distribution**:
   - `Beta(successes + 1, failures + 1)`

3. At every round:
   - Sample a random value from each ad's Beta distribution  
   - Choose the ad with the highest sample  
   - Observe reward (0 or 1)  
   - Update successes/failures  

**Why it works**:  
Better ads tend to give higher samples more often,  
but randomness keeps exploring other ads sometimes.

**Strengths**:
- Very strong performance  
- Naturally balances exploration/exploitation  
- Works well even with limited data  

---

## 🧠 Algorithm 2: UCB1 (Upper Confidence Bound)

**Idea**:  
Pick the ad that has the best balance between:
- its average reward so far  
- and the "confidence" that we still don’t know enough about it  

In simple words:
> Choose the ad with the highest “potential upper bound.”

**How it works**:
1. For each ad, track:
   - how many times it was chosen  
   - its average reward  

2. At each round:
   Calculate:
   \[
   \text{UCB}_i = \text{average reward} + \sqrt{\frac{2 \ln(n)}{n_i}}
   \]
   where:
   - `n` = round number  
   - `n_i` = how many times ad *i* was selected  

3. Pick the ad with the highest UCB score.

**Why it works**:
- Ads with high success look good  
- Ads with low trials get a “bonus” for exploration  
- The formula shrinks the bonus over time  

**Strengths**:
- Deterministic (no randomness)  
- Good theoretical guarantees  

---

## 🆚 Summary: Thompson Sampling vs UCB1

| Feature | Thompson Sampling | UCB1 |
|--------|-------------------|-------|
| Exploration | Random (Bayesian) | Mathematical confidence bonus |
| Stability | Smooth | More aggressive early exploration |
| Ease of Understanding | Medium | Simple formula |
| Typical Performance | Often the best | Very good |

Both algorithms learn the best ad over time, but Thompson Sampling usually converges more efficiently in practice.

---

## 📂 Project Contents

The folder contains:
- Implementation of **Thompson Sampling**
- Implementation of **UCB1**
- The dataset used for simulations
- Plots showing how often each ad was selected

You can directly compare the two algorithms using the same environment.

---

## ✔ Purpose of the Project

This project helps you clearly understand:
- How Multi-Armed Bandit problems work  
- How reinforcement learning solves exploration vs exploitation  
- The difference between classical (UCB1) and Bayesian (Thompson Sampling) approaches  
- How these algorithms can be applied to real-world decision-making  

