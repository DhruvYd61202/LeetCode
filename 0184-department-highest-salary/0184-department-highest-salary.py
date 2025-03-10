import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # department.rename({'id' : 'departmentId'}, inplace=True)
    merged_df = employee.merge(department, how='left',left_on='departmentId', right_on='id')

    highest_salary = merged_df.loc[merged_df.groupby('departmentId')['salary'].transform('max') == merged_df['salary']]

    result = highest_salary[['name_x', 'salary', 'name_y']].rename(columns={ 
        'name_y': 'Department',  # department name column
        'name_x': 'Employee',    # employee name column
        'salary': 'Salary'       # salary column
    })
    return result[['Department', 'Employee', 'Salary']]



    