from fastmcp import FastMCP
import time
import sys

mcp = FastMCP(
    name='count_occurence',
)

@mcp.tool()
def count_occurence(word: str, letter: str) -> int:
    """
    Counts the number of occurrences of a given letter in a word.
    """
    try:
        return word.lower().count(letter.lower())
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    try:
        print("Starting the MCP server..")
        mcp.run()
    except KeyboardInterrupt:
        print("\nStopping the MCP server...")
        time.sleep(1)
    except Exception as e:
        sys.stderr.write(f"Exception while running MCP server: {e}\n")
