export default function Navbar() {
    return (
        <nav class="flex flex-row items-center py-4 px-[10%] justify-between">
            <a href="#" class="text-3xl">Stack<b>Learning</b></a>
            <ul class="flex">
                <li>
                    <a href="#" class="block font-medium p-3 m-2">Home</a>
                </li>
                <li>
                    <a href="#" class="block font-medium p-3 m-2">Create</a>
                </li>
                <li>
                    <a href="#" class="block font-normal p-3 bg-[#6c63ff] text-white rounded-lg m-2">Get started</a>
                </li>
            </ul>
        </nav>
    )
}