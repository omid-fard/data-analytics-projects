# =====================================================
# Project: Business Performance Analysis
# File: run_pipeline.py
# Purpose: Run the complete end-to-end data pipeline
# =====================================================

from pathlib import Path
import argparse
import subprocess
import sys
import time


# =====================================================
# Paths
# =====================================================

PYTHON_DIR = Path(__file__).resolve().parent

GENERATE_SCRIPT = (
    PYTHON_DIR
    / "generate_sample_data.py"
)

PREPARE_SCRIPT = (
    PYTHON_DIR
    / "prepare_data.py"
)

LOAD_SQL_SCRIPT = (
    PYTHON_DIR
    / "load_to_sql.py"
)


# =====================================================
# Pipeline Steps
# =====================================================

PIPELINE_STEPS = [
    (
        "Generate Sample Data",
        GENERATE_SCRIPT,
    ),
    (
        "Prepare and Validate Data",
        PREPARE_SCRIPT,
    ),
]


# =====================================================
# Run Script
# =====================================================

def run_script(
    step_name,
    script_path,
):

    print(
        "\n==================================="
    )

    print(
        f"STARTING: {step_name}"
    )

    print(
        "==================================="
    )

    if not script_path.exists():

        raise FileNotFoundError(
            f"Script not found: "
            f"{script_path}"
        )

    start_time = time.time()

    subprocess.run(
        [
            sys.executable,
            str(script_path),
        ],
        check=True,
    )

    elapsed_time = (
        time.time()
        - start_time
    )

    print(
        "\n-----------------------------------"
    )

    print(
        f"COMPLETED: {step_name}"
    )

    print(
        f"Execution time: "
        f"{elapsed_time:.2f} seconds"
    )

    print(
        "-----------------------------------"
    )


# =====================================================
# Command-Line Arguments
# =====================================================

parser = argparse.ArgumentParser(
    description=(
        "Run the Business Performance "
        "Analysis data pipeline."
    )
)

parser.add_argument(
    "--skip-sql",
    action="store_true",
    help=(
        "Run data generation and ETL "
        "without loading data into "
        "SQL Server."
    ),
)

args = parser.parse_args()


# =====================================================
# Main Pipeline
# =====================================================

def main():

    pipeline_start = time.time()

    print(
        "\n==================================="
    )

    print(
        "BUSINESS PERFORMANCE ANALYSIS"
    )

    print(
        "END-TO-END DATA PIPELINE"
    )

    print(
        "==================================="
    )

    print(
        "\nPipeline steps:"
    )

    print(
        "1. Generate synthetic raw data"
    )

    print(
        "2. Clean and transform data"
    )

    if args.skip_sql:

        print(
            "3. SQL Server load: SKIPPED"
        )

    else:

        print(
            "3. Load data into SQL Server"
        )


    # ================================================
    # Step 1 and Step 2
    # ================================================

    for (
        step_name,
        script_path,
    ) in PIPELINE_STEPS:

        run_script(
            step_name,
            script_path,
        )


    # ================================================
    # Step 3 - SQL Server
    # ================================================

    if not args.skip_sql:

        run_script(
            "Load Data into SQL Server",
            LOAD_SQL_SCRIPT,
        )


    # ================================================
    # Pipeline Summary
    # ================================================

    total_time = (
        time.time()
        - pipeline_start
    )

    print(
        "\n==================================="
    )

    print(
        "PIPELINE COMPLETED SUCCESSFULLY"
    )

    print(
        "==================================="
    )

    print(
        f"Total execution time: "
        f"{total_time:.2f} seconds"
    )

    if args.skip_sql:

        print(
            "\nSQL Server loading was skipped."
        )

        print(
            "Processed CSV files are ready "
            "for analysis."
        )

    else:

        print(
            "\nData generation, ETL, and "
            "SQL Server loading completed."
        )

    print(
        "\nThe data is ready for "
        "Power BI reporting."
    )


# =====================================================
# Entry Point
# =====================================================

if __name__ == "__main__":

    try:

        main()

    except subprocess.CalledProcessError as error:

        print(
            "\n==================================="
        )

        print(
            "PIPELINE FAILED"
        )

        print(
            "==================================="
        )

        print(
            f"A pipeline step returned "
            f"exit code {error.returncode}."
        )

        sys.exit(
            error.returncode
        )

    except Exception as error:

        print(
            "\n==================================="
        )

        print(
            "PIPELINE FAILED"
        )

        print(
            "==================================="
        )

        print(
            f"Error: {error}"
        )

        sys.exit(1)
