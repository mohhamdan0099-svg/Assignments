var student={
    firstName:"Maya",
    course:"Full Stack Development",
    learningTopics:["objects","functions","this"],
    completedLessons:3,
    totalLessons:5,
    getProgressMessage: function(){
        var percentage=(this.completedLessons / this.totalLessons)*100;
        return this.firstName + "finished" + percentage + "% of the lessons.";

    }
};

function getLearningPlan(learner){
    return learner.firstName + "is practicing" + learner.Topics.join(",")+".";
}

function printMessage(message){
    console.log("MESSAGE:"+ message.toUpperCase());
}

console.log(getLearningPlan(trainee));
printMessage(getLearningPlan(student));
const progressMessage = student.getProgressMessage;
console.log(progressMessage());