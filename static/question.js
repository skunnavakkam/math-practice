
// first we have a data object
// due to this, the loading of this NEEDS to be defered

const data = data

var question = data["question"]
var answer = data["answer"]
var solution = data["solution"]

var isMultipleChoice = Array.isArray(answer)

document.getElementById("question-div").innerHTML = question

if (isMultipleChoice) {
    const answerForm = document.getElementById('answerForm')


} 
else {

}
