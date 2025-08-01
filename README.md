# Performance Benchmarks with ASV

A test to demonstrates performance tracking over time using ASV

## Setup

```bash
pip install asv
```

## How to Add a New Performance Point

### Step 1: Modify benchmarks to simulate performance change

For performance improvement, edit `benchmarks/benchmarks.py`:
- Reduce loop iterations
- Reduce data sizes 
- Simplify calculations

For performance regression:
- Increase loop iterations
- Add more complex calculations
- Increase data processing

### Step 2: Create a new version

```bash
# Make your changes to benchmarks/benchmarks.py
git add -A
git commit -m "v2.6.0: Your performance change description"  # Use your version number
git tag v2.6.0  # Use your own version number (v2.6.0, v2.7.0, etc.)
```

### Step 3: Run benchmarks on the new version

```bash
asv run v2.6.0^!  # Replace with your version number
```

### Step 4: Update graphs

```bash
asv publish
asv preview
```

### Step 5: View results

Open http://localhost:8080 to see the new data point on the graphs.

## Current Benchmark History

- v2.1.0: Initial test benchmarks
- v2.2.0: Performance optimizations 
- v2.3.0: Feature expansion (regression)
- v2.4.0: Partial recovery
- v2.5.0: Major optimization breakthrough

Each  shows different performance patterns in the ASV graphs