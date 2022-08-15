import Navbar from './components/Navbar'
import CallToAction from './components/CallToAction'
import Info from './components/Info'

import './index.css'

function App() {
  return (
    <div>
      <div class="bg-slate-100 h-screen">
        <Navbar />
        <CallToAction />
      <div class="flex flex-row pt-9 pl-[10%] pr-[10%]">
        <Info icon="fa-solid fa-person-arrow-up-from-line fa-2x" header="Stand out from your peers." paragraph="Students who use StackLearning are more likely to report a higher grade than their peers."/>
        <Info icon="fa-solid fa-repeat fa-2x" header="Repetition is key" paragraph="Your study stacks are built like a carousel, so you can continuously review your cards without interruption."/>
        <Info icon="fa-regular fa-heart fa-2x" header="Made by students, for students." paragraph="Your benefit is our in our #1 interest, this is why we've made StackLearning to be ad-free, cost-free, and straightforward, forever."/>
      </div> 
      </div>
    </div>
  )
}
export default App;
