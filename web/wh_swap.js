import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "ComfyUI.WHSwap",

    async nodeCreated(node) {
        if (node.comfyClass !== "WidthHeightSwap") {
            return;
        }

        const swapWidget = node.addWidget(
            "button",
            "↔ Swap Width / Height",
            null,
            () => {
                const widthWidget = node.widgets?.find((w) => w.name === "width");
                const heightWidget = node.widgets?.find((w) => w.name === "height");

                if (!widthWidget || !heightWidget) {
                    return;
                }

                const oldWidth = widthWidget.value;
                widthWidget.value = heightWidget.value;
                heightWidget.value = oldWidth;

                // Notify ComfyUI that the node changed.
                widthWidget.callback?.(widthWidget.value);
                heightWidget.callback?.(heightWidget.value);

                node.setDirtyCanvas(true, true);
                app.graph?.setDirtyCanvas(true, true);
            }
        );

        swapWidget.serialize = false;
    },
});
