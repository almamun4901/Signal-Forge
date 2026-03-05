# SignalForge

SignalForge is a machine learning–based quantitative research project for generating and evaluating stock trading signals.

The goal of the project is to explore whether machine learning models trained on financial market data can predict short-term stock returns and generate profitable investment strategies.

## What the Project Consists Of

SignalForge follows a typical quantitative research pipeline:

1. **Market Data**
   - Historical stock price and volume data.

2. **Feature Engineering**
   - Financial factors (Alpha158) derived from price and volume.

3. **Machine Learning Model**
   - LightGBM model trained to predict next-day stock returns.

4. **Signal Generation**
   - Stocks are ranked by predicted return scores.

5. **Portfolio Strategy**
   - A portfolio is constructed by selecting top-ranked stocks.

6. **Backtesting**
   - Trading strategies are simulated using historical data.

7. **Performance Evaluation**
   - Metrics such as annual return, information ratio, and drawdown are calculated.

## Goal

The main goal of SignalForge is to build a research environment for:

- testing machine learning–based alpha signals
- evaluating quantitative trading strategies
- understanding the effectiveness of financial factors

This project is intended as a **quantitative research experiment**, not a production trading system.

## Pipeline

1. **Market Data**
2. **Feature Engineering**
3. **ML Model**
4. **Signal Generation**
5. **Portfolio Strategy**
6. **Backtesting**


## Components

**Market Data**
- Historical price and volume data

**Feature Engineering**
- Alpha158 factor set derived from market data

**Machine Learning Model**
- LightGBM model used to predict next-day returns

**Signal Generation**
- Stocks ranked by predicted return scores

**Portfolio Strategy**
- Top-ranked stocks selected to construct a portfolio

**Backtesting**
- Strategy performance simulated using historical data

**Evaluation**
- Performance measured using metrics such as:
  - annualized return
  - information ratio
  - max drawdown

## Purpose

SignalForge is designed as a **quantitative research environment** for experimenting with machine learning–based trading signals and evaluating their effectiveness through systematic backtesting.