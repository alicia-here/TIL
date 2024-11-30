import pandas as pd
from IPython.display import display

def explore_data(data):
    """
    데이터프레임의 기본 정보를 출력합니다.
    각 열의 유니크 값 개수와 목록, 결측치 및 중복 데이터를 확인합니다.
    """
    print("=== 데이터 기본 정보 ===")
    display(data.info())
    print("\n=== 컬럼별 유니크 값 확인 ===")
    for column in data.columns:
        print(f"\n컬럼명: {column}")
        print(f"- 데이터 타입: {data[column].dtype}")
        print(f"- 결측치 개수(비율): {data[column].isnull().sum()} ({data[column].isnull().mean() * 100:.2f}%)")
        print(f"- 유니크 값 개수: {data[column].nunique()}")
        print(f"- 유니크 값: {data[column].unique()[:10]}{'...' if data[column].nunique() > 10 else ''}")
    print("\n=== 중복 데이터 확인 ===")
    duplicates = data[data.duplicated()]
    if not duplicates.empty:
        print(f"중복된 행 수: {len(duplicates)}")
        display(duplicates)
    else:
        print("중복 데이터 없음.")
    print("\n=======================\n")


def view_datetime_range(data, column):
    """
    datetime 형식의 컬럼에서 데이터의 첫 시간(최초시간)과 마지막 시간(최후시간)을 출력합니다.
    """
    print(f"=== {column} 컬럼의 시간 범위 ===")
    try:
        datetime_series = pd.to_datetime(data[column])
        print(f"- 최초 시간: {datetime_series.min()}")
        print(f"- 최후 시간: {datetime_series.max()}")
    except Exception as e:
        print(f"오류: {e} - {column} 컬럼을 datetime 형식으로 변환할 수 없습니다.")
    print("\n=======================\n")
