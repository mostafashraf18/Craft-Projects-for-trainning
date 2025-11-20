import promptSync from "prompt-sync";

const empName = "Youssef";
const empSalary = 1200;
const empStartDate = 2020;

function calculateYearsInService(startDate: number) {
    return new Date().getFullYear() - startDate;
}

function calculateBomus(salary: Number){
    return Math.floor(salary * 0.10)
}

function printEmployeeInfo(name: string, salary: Number, startDate: Number){

    console.log('Name: '+ name);
    console.log("Salary: ", salary);
    console.log("Years in service: ");
    console.log('Bonus: ')
}
