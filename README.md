# hugo_research
## Introduction
This repository contains the methodology and code for my research project made under supervision of Hugo Schyns.
## Advice from Hugo
### Data cleaning
* What to do when companies change their TIC code, use CUSIP?  
Read up on the litterature about this subject. Hugo told me that many financial analysts/auditors use CUSIP.
* Missing values?  
Approach mentioned in the paper and also supported by Hugo:
    1. If possible, fill forward.
    2. If not possible, compute median from cross-section.
* How do you handle string values, one-hot encoding?  
There are no string values.
### Data structuring
* Training, validition and test sample: do this in a rolling window, but which kind is best (there are three main methods)?  
Hugo suggested to first structure your time series into multiple windows (e.g. 12/3,23/4, etc.) and then use one of the two possibilities:
    1. Randomly select windows for training set and test set. This generalises better, but kind of look like data leakage to me.
    2. Select first x% for training and last (100-x)% for test.

## Content
### 1. Selection
* revenue (TTM) = revtq
* cost of goods sold (TTM) = cogsq
* selling, general & and admin expense (TTM) = xsgaq
* net income (TTM) = niq
* earnings before interest and taxes or EBIT (TTM): ebitq = revtq - xoprq - dpq 

* cash and cash equivalents (MRQ) = used cheq for now <=> chechy <!---FIXME: this is yearly, not quarterly--->
* receivables (MRQ) = rectq
* inventories (MRQ) = invtq
* other current assets (MRQ) = acoq
* property plant and equipment (MRQ) = ppegtq
* other assets (MRQ) = aoq
* debt in current liabilities (MRQ) = dlcq
* accounts payable (MRQ) = uaptq
* taxes payable (MRQ) = txpq
* other current liabilities (MRQ) = lcoq
* total liabilities (MRQ) = ltq

* price movement of the stock over the previous 1, 3, 6, and 9 months => compute manually

### 2. Preprocessing
FIXME: add info.
### 3. Modeling