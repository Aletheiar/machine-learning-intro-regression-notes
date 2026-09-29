# 机器学习零基础讲义：导论与回归

这份中文讲义供机器学习初学者个人预习、复习和查阅。内容覆盖机器学习的基本框架、学习范式、泛化，以及回归中的 K 近邻、线性回归、梯度下降、正则化和模型评估。讲义还包含手算例子、Python 练习、自测题与参考答案。它对应课程前两讲，并非整门机器学习课程。

- [阅读 PDF](机器学习零基础讲义.pdf)
- [编辑 TeX 源码](机器学习零基础讲义.tex)
- [指标计算示例](examples/metrics.py)
- [回归工作流示例](examples/regression.py)
- [第一讲课件：机器学习简介](<机器学习简介 · 第一讲 (1).pptx>)
- [第二讲课件：回归](<机器学习导论 · 第 2 讲：回归.pptx>)

## 使用方法

第一次阅读可先看讲义第 1--7 章和第 10 章，再读矩阵推导与正则化的进阶部分，最后运行代码和做自测题。

指标计算示例仅需 Python 标准库。回归工作流示例需要 NumPy 和 scikit-learn：

```bash
python -m pip install numpy scikit-learn
python examples/metrics.py
python examples/regression.py
```

如需重新编译 PDF，可使用支持 `ctexbook` 的 XeLaTeX 环境或 Tectonic：

```bash
tectonic 机器学习零基础讲义.tex
```

当前 PDF 适合阅读；某些 PDF 文本提取工具对其中的中文字符支持不佳，查找或复制中文时可使用 TeX 源码。

## 资料说明

讲义根据本仓库的两份 PPTX 和《回归：从条件期望到正则化》（`2-regression.pdf`）重新组织与补充。两份 PPTX 已获授权公开；补充 PDF 未上传。本仓库的示例数据用于教学，不能视作真实房价或产品性能证据。第二讲中的一处三点最小二乘演示数值已在讲义第 6 章重新核算。
