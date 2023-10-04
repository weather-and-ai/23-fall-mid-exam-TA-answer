# Judge part

### Create a `.csv` file to store students' scores
```shell
echo "studentId,score" > hw00.csv
```

### Find all files that start with `HW___` and end with `.ipynb`
```shell
ipynb_files=$(find . -name "HW___*.ipynb")
```

### Parse the `.ipynb` file using the `jq` tool

```shell
output=$(jq -r '.cells[nums].outputs[0].text' "$file")
```
