# Python Scrabble AI

> **Disclaimer:** This repository contains an academic project developed for the Programming Fundamentals (FP) course at Instituto Superior Técnico (IST). It is shared for portfolio purposes only. Current students should adhere to academic integrity guidelines.

## Overview

A fully functional, text-based implementation of the classic Scrabble game, written entirely in Python. The project evolved from a basic rule-enforcement engine into a complete game built on Abstract Data Types (ADTs), with AI bots capable of playing against human opponents.

## Features

- **Abstract Data Types (ADTs)** — Encapsulation and abstraction barriers used throughout to manage the Board (`tabuleiro`), Players (`jogador`), Vocabulary (`vocabulario`), and Board Cells (`casa`).
- **AI Agents** — Three difficulty levels (Easy, Medium, Hard). Each agent generates all viable board patterns and searches the vocabulary for the highest-scoring valid word.
- **Custom Algorithms** — A Fisher–Yates shuffle and a 32-bit Xorshift pseudo-random number generator, used to manage the letter bag fairly.
- **Rule Engine** — Full validation of vocabulary, scoring (including letter values and bonus tiles), and board boundaries.
- **State Management** — Tracks player turns, scores, remaining letters, and end-game conditions.

## Tech Stack

- **Python 3** — procedural and functional programming paradigms
