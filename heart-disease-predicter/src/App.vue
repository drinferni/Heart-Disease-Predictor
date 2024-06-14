<template>

<div>

  <div>
  <label>Enter Your Age</label>
  <input type="number" v-model="age" placeholder="18">
  </div>


  <div>
    Gender
    <input type="radio" value="1" v-model="gender" >
    <input type="radio" value="0" v-model="gender">
  </div>

  <div>
    <label>Please enter Cholestrol level</label>
    <input type="number" v-model="cholesterol" placeholder="in mg/dL">
  </div>

  <div>
    <div >
        Are you a smoker
        <input type="checkbox" value="1" v-model="ever_smoked" >
    </div>
    <div v-if="ever_smoked">
      Have you quit?
      <input v-if="ever_smoked" type="checkbox" value="0" v-model="is_smoking">
    </div>


  </div>
  
  <div>
    <div>
      Do you drink alcohol
    <input type="checkbox" value="true" v-model="drinker" >
  </div>

    <div v-if="drinker==true">
      Is your consumption of alochol high?
      <input v-if="drinker==true" type="checkbox" value="true" v-model="Heavy_drinker">
    </div>

  </div>

  <div>
    <label>How many hours do you excercise per week?</label>
    <input type="number" v-model="Exercise_Hours">
  </div>

  <div>
    <label>do you have a family history of heart disease?</label>
    <input type="radio" v-model="Family_History" value="1"> 
  </div>

  <div>
    <label>Are you obese?</label>
    <input type="radio" v-model="Obesity" value="1"> 
  </div>

  <div>
    <label>Do you have diabeties?</label>
    <input type="radio" v-model="Diabetes" value="1"> 
  </div>

  <div>
    <label>From 0 to 10 what are your stress levels</label>
    <input type="number" id="rating" v-model="Stress_Level" min="0" max="10" placeholder="from 0 to 10">
  </div>

  <div>
    <label> Do you experience excercise induced angina?</label>
    <input type="radio" v-model="Exercise_Induced_Angina" value="1"> 
  </div>

  <div>
    <button @click="predict" type="submit">Submit</button>
  </div>
  

</div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
      return {
        age: 0,
        gender:0,
        cholesterol:0,
        heartrate:0,
        ever_smoked:0,
        is_smoking:0,
        drinker:0,
        Non_drinker:1,
        Heavy_drinker:0,
        Exercise_Hours:0,
        Family_History:0,
        Diabetes:0,
        Obesity:0,
        Stress_Level:0,
        Exercise_Induced_Angina:0
      }
  },
  methods :{ 

    predict () {
      if (this.drinker) this.Non_drinker = 0
      else this.Non_drinker = 1


      let data = [];
      data.push(this.age)
      data.push(this.gender)
      data.push(this.cholesterol)
      data.push(this.heartrate)
      data.push(this.ever_smoked)
      data.push(this.is_smoking)
      data.push(this.Non_drinker)
      data.push(this.Heavy_drinker)
      data.push(this.Exercise_Hours)
      data.push(this.Family_History)
      data.push(this.Diabetes)
      data.push(this.Obesity)
      data.push(this.Stress_Level)
      data.push(this.Exercise_Induced_Angina) 

      console.log(data)
      
      axios.post('http://127.0.0.1:5000/data', {
  key: data
})
.then(response => {
  console.log('Response:', response.data);
  // Handle success scenario here
})
.catch(error => {
  console.error('Error:', error);
  // Handle error scenario here
});

      

    }

  },
}
</script>

<style>

</style>
