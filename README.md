# Quantamental Investing Research

Python research experiments connecting market signals with a fundamental investor's perspective.

**Xavier Chen · Finance, research, and automation**  
**Status:** Exploratory analysis. Historical outputs are not independently verified performance.

## Project description

My background in audit, accounting, and FP&A motivates a practical question: how can systematic tools broaden research coverage and make investment analysis more repeatable without losing financial context?

The repository brings together VIX-based index-exposure experiments, a market-sentiment notebook, and a personal portfolio report. The focus is developing and critically reviewing methods, not promising a target return or Sharpe ratio.

## Research map

| Component | Start here |
| --- | --- |
| SPY/VIX experiment | [Reviewed notebook](VIX_for_Index_Strengthen/VIX%20strategy%20on%20SPY_Index%20enhancement.ipynb) · [Extracted calculation script](VIX_for_Index_Strengthen/spy_experiment.py) |
| Other index experiments | [Research idea](VIX_for_Index_Strengthen/My_Ideas.md) · [QQQ and DIA notebooks](VIX_for_Index_Strengthen/) |
| Market sentiment | [Overview](Market_Sentiment_Monitor/Readme.md) · [Notebook](Market_Sentiment_Monitor/Market%20Sentiment%20monitor.ipynb) |
| Portfolio record | [Dated report folder](Chen%27s%20Portfolio%20Performance/) |

## Important SPY methodology clarification

The October 3, 2026 review corrected the SPY notebook's QQQ introduction, misleading buy/sell labels, daily-position explanation, and chart presentation. Its financial calculations and exposure parameters are retained, now in a readable adjacent Python script.

**The existing code takes 1.9x long SPY exposure when VIX is below 15, and 1.0x otherwise.** The variable `short_position` does not mean short-selling. The neutral band resets daily; it does not retain the preceding day's exposure.

Previously cached outputs have been cleared from the reviewed notebook rather than presented as new results. The [exact original notebook](archive/vix-spy-original-2026-10-03.ipynb) is preserved with its old outputs for comparison. It is a historical archive, not an endorsed result.

The reviewed script passed a local Python syntax check. The historical analysis was **not rerun** against market data, and the QQQ/DIA notebooks have not received the same review. These are distinct from the tested synthetic bond example in the separate fixed-income repository.

## Tech stack and installation

Python, Jupyter notebooks, and notebook-specific analytical libraries. The original notes identify Yahoo Finance as a market-data source and local models for company analysis.

```bash
git clone https://github.com/Xiaowen-CHEN-Learner/Quantitative-investing_Quantamental-approach.git
cd Quantitative-investing_Quantamental-approach
python -m venv .venv
```

Activate with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in PowerShell. For the SPY example:

```bash
python -m pip install jupyterlab yfinance pandas numpy matplotlib
python -m jupyterlab
```

This is an installation recipe, not a tested version lock. Other notebooks may require additional libraries. Inspect imports and local-file references before execution.

## Usage

Open the reviewed SPY notebook with its kernel working directory set to `VIX_for_Index_Strengthen`, then run its cell. Alternatively run `python VIX_for_Index_Strengthen/spy_experiment.py` from the repository root.

Record source-data retrieval dates, package versions, observation dates, and failures. Before interpreting output, establish when the signal is observable and how a trade could actually be executed.

## Validation priorities and limitations

Same-close execution, financing for leveraged exposure, fees, slippage, cash returns, provider column ordering, benchmark alignment, drawdown initialization, and out-of-sample testing require explicit treatment. A shifted signal alone does not resolve execution assumptions. Dynamic date windows and changing provider data can change results between runs.

Add a permitted sample dataset and a tested dependency specification before describing the historical notebooks as reproducible. Reduce the large sentiment notebook's embedded output only after preserving representative evidence. A personal report is not an audited track record.

## Contributing and attribution

Open an issue with the affected notebook, reproduction steps, and proposed methodological improvement. The October 2026 documentation/code-structure review was AI-assisted; it does not establish independent validation of the investment research. Do not upload proprietary models, credentials, or restricted datasets.

[Xavier Chen on LinkedIn](https://www.linkedin.com/in/xiaowen-chen/) · [GitHub portfolio](https://github.com/Xiaowen-CHEN-Learner)

## License

No project-wide license is included. Third-party data and documents retain applicable rights and restrictions.

---

Educational research only. Not investment advice.
