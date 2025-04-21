from rich.console import Console
from rich.panel import Panel
from rich import box
import time

console = Console()

class LiveChatUI:
    def show_message(self, msg):
        panel = Panel(msg.content, title=f"{msg.sender} → {msg.receiver}", box=box.ROUNDED, style="cyan")
        console.print(panel)
        time.sleep(1)

    def show_end(self):
        console.print("[bold green]✅ A2A Conversation Complete[/bold green]\n")
