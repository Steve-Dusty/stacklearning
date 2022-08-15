// trophy icon: <i class="bi bi-trophy"></i>
// bullseye icon: <i class="bi bi-bullseye"></i>
// lightbulb icon: <i class="bi bi-trophy"></i>
export default function Info({ icon, header, paragraph }) {
    return (
        <div class="flex flex-row basis-full">
            <div>
                <i class={icon}></i>
            </div>
            <div class="flex-column pl-5">
                <h2 class="text-lg font-semibold">{header}</h2>
                <p class="text-sm">{paragraph}</p>
            </div>
        </div>
    )
}