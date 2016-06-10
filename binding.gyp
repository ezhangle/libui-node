{
	"targets": [
		{
			"includes": [
				"auto.gypi"
			],
			"sources": [
				"src/Ui.cc",
				"src/UiWindow.cc",
				"src/UiControl.cc",
				"src/UiEntry.cc",
				"src/UiLabel.cc",
				"src/UiButton.cc",
				"src/UiCheckbox.cc",
				"src/UiBox.cc"
			],
			"libraries": [
				"../libui/build/out/libui.so"

			]
		}
	],
	"includes": [
		"auto-top.gypi"
	]
}
