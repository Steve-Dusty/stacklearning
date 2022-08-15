import Image from '../assets/images/undraw_image.svg'

export default function CallToAction() {
    return (
        <div class="flex flex-row px-[10%] p-12">
            <div class="w-2/5">
                <h1 class="text-5xl font-bold text-[#6c63ff] pb-5">Memorize Smarter For Your Next Exam</h1>
                <p class="text-lg underline decoration-yellow-500/60 pb-14">Accelerate your learning by using the only study tool you'll ever need</p>
                <button class="text-lg bg-green-300 p-3 rounded-lg font-semibold mt-9">Get Started</button>
            </div>
            <img class="w-3/5" src={Image} alt="person climbing a stack of books"/>
        </div>
    )
}
