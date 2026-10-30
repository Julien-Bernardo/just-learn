# Figures

`assets/homework-vs-exam-*.svg` (the chart at the top of the main README) is a redraw of Figure A11 in Strömberg, Lei & Wu (2026), ["The Generative AI Learning Penalty: Evidence from Chinese Secondary Education"](https://ssrn.com/abstract=6868618).

The figure in the paper's PDF is vector graphics, so `a11_digitised.json` holds the exact points from its paths, converted to the axis scale: the smoothed mean exam score by homework score, and the 95% confidence band, for AI users (`ai_*`) and students who never used AI (`noai_*`). Both axes are scaled so the average without AI is 100. The data is observational, so the chart shows a pattern, not cause and effect.

To regenerate the charts:

```bash
python3 research/figures/make_chart.py research/figures/a11_digitised.json assets
```
