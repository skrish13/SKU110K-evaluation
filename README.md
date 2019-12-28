# SKU110K-evaluation

Evaluation code for SKU110K dataset. Forked from [cocoapi](https://github.com/cocodataset/cocoapi) repository.

### Steps
- Place the `annotations_test.csv` inside `groundtruth` folder. Data can be obtained from here [1].
- Place your predictions.csv inside `predictions` folder.
- Run `calc_acc.py` inside `cocoapi/PythonAPI/pycocotools` after modifying the predictions file path.

### Results

| Method  | AP | AP<sup>.75</sup> | AR<sup>300</sup>  |
| ----- | ----- | ---- | ----- |
|Goldman et al [2]| 0.492 | 0.556 |0.554  |
|Our method [3]| 0.186 |0.052 | 0.264 |

### References

```
[1] https://github.com/eg4000/SKU110K_CVPR19
[2] https://arxiv.org/abs/1904.00853
[3] https://github.com/ParallelDots/generic-sku-detection-benchmark
```
