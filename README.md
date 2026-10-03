# Quantamental Investing Research

Python notebook experiments combining market signals with a fundamental investor's perspective.

**Author:** Xavier Chen · Finance, research, and automation  
**Status:** Exploratory research. Notebook outputs are historical experiments, not independently verified investment performance.

## Project description

My background in audit, accounting, and FP&A motivates a practical question: how can systematic tools broaden research coverage and make investment analysis more repeatable without losing financial context?

This repository brings together VIX-based index-strategy experiments, a market-sentiment notebook, and a personal portfolio report. The emphasis is on developing and critically evaluating research methods, rather than promising a target return or Sharpe ratio.

## Research map

| Component | What is available | Where to start |
| --- | --- | --- |
| VIX/index experiments | Separate notebooks labelled SPY, QQQ, and DIA | [Research idea](VIX_for_Index_Strengthen/My_Ideas.md) · [Notebooks](VIX_for_Index_Strengthen/) |
| Market sentiment | A market-sentiment monitoring notebook | [Overview](Market_Sentiment_Monitor/Readme.md) · [Notebook](Market_Sentiment_Monitor/Market%20Sentiment%20monitor.ipynb) |
| Portfolio record | A dated personal portfolio report | [Report folder](Chen%27s%20Portfolio%20Performance/) |

**Suggested first review:** [VIX strategy on SPY](VIX_for_Index_Strengthen/VIX%20strategy%20on%20SPY_Index%20enhancement.ipynb). Its introductory text currently refers to QQQ, so reconcile the narrative, code ticker, and benchmark before relying on the output. The SPY filename alone is not sufficient validation.

## Tech stack

Python and Jupyter notebooks. The original research notes identify Yahoo Finance as a market-data source and describe company analysis using local financial models. Availability and licensing of source data should be checked before reuse.

A tested, pinned dependency manifest is not yet included. Package imports and any notebook-specific installation cells must be reviewed before execution.

## Installation

To browse the notebooks, use GitHub's notebook viewer; no local installation is necessary.

For local inspection:

```bash
git clone https://github.com/Xiaowen-CHEN-Learner/Quantitative-investing_Quantamental-approach.git
cd Quantitative-investing_Quantamental-approach
python -m venv .venv
```

Activate the environment with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in Windows PowerShell. Then install the notebook interface:

```bash
python -m pip install jupyterlab
python -m jupyterlab
```

This installs the interface only, not all analytical dependencies. Inspect the selected notebook's imports and install the required packages in the same environment. A clean-environment reproduction has not been established by the documentation update.

## Usage

1. Read the research idea and identify the proposed signal, asset, benchmark, and observation period.
2. Inspect the notebook before executing it, including data downloads and local file references.
3. Confirm that the signal is observable before the assumed trade execution time.
4. Restart the kernel and run cells in order. Record package versions, the data retrieval date, and any failures.
5. Compare results against a consistent benchmark and document risk, turnover, transaction-cost assumptions, and out-of-sample behaviour.

## Validation priorities

- Reconcile asset labels and introductory descriptions across SPY, QQQ, and DIA notebooks.
- Specify signal timing, execution prices, dividends, adjusted prices, cash returns, fees, and slippage.
- Separate parameter selection from out-of-sample evaluation and test sensitivity to dates and thresholds.
- Check missing data, date alignment, look-ahead bias, and benchmark comparability.
- Add a dependency manifest, small permitted sample dataset, and automated checks.
- Reduce embedded notebook output size while keeping a concise, reproducible report of the main findings.

These are review priorities, not a claim that every listed issue has been found or fixed.

## Results and limitations

Existing outputs reflect the data and assumptions used when each notebook was run. They have not been independently reproduced as part of this documentation update. A personal portfolio report is not an audited track record, and neither historical returns nor a backtest establish future performance.

## Contributing

Open an issue with the notebook name, research question, reproduction steps, and the proposed change. Improvements to methodology, data validation, and reproducibility are particularly welcome. Do not upload proprietary financial models, credentials, or restricted datasets.

## Author and contact

[Xavier Chen on LinkedIn](https://www.linkedin.com/in/xiaowen-chen/) · [GitHub portfolio](https://github.com/Xiaowen-CHEN-Learner)

## License

No project-wide license is currently included. Third-party data and documents retain their applicable rights and restrictions.

---

Educational and research use only. Not investment advice.
